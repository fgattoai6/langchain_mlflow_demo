
import os
import json
import mlflow
from dotenv import load_dotenv  
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from mlflow.entities.model_registry.prompt_version import PromptVersion
from schemas.damage_report_fr import MultiDamageReport
from schemas.data_prep_rules import LIST_TEXT, UNITS_TEXT, RULES_TEXT

def inference(agent0, agent1, prompt0, prompt1, prompt2, input_transcript) ->MultiDamageReport:
    # key "function" input is ~here. not before, not after (I keep tracing but  reject the run)
    with mlflow.start_span("p6p", attributes={"input_transcript":str(input_transcript) }) as allrunspan:
        allrunspan.set_inputs({"transcript_len": len(input_transcript), "transcript_preview": input_transcript})
        allrunspan.set_attribute("prompt_stage", "3-step pipeline: alignment → structured → final")
        #===========================
        # Agent0
        #===========================
        with mlflow.start_span("semantic_alignment") as span0:
            span0.set_attribute("stage", "agent0")
            formated_prompt = prompt0.format(transcript=input_transcript)
            response = agent0.invoke({"messages": formated_prompt})
            response_text = response["messages"][-1].content
            span0.set_outputs({"aligned_text_len": len(response_text), "preview": response_text})
            mlflow.log_text(response_text, "semantic_alignment.txt")

        #===========================
        # Agent1
        #===========================
        with mlflow.start_span("structured_output") as span1:
            span1.set_attribute("stage", "agent1")
            # result = agent_2.invoke({
            #     "messages": [{"role": "user", "content": f"Extrait les dégats constaté dans la description suivante: \n{response_text}"}] 
            # })
            formated_prompt1 = prompt1.format(unit_text=UNITS_TEXT, liste_text=LIST_TEXT, user_text=response_text)
            out1 = agent1.invoke({"messages": formated_prompt1})
            structured_report  = out1["messages"][-1].content
            # result:MultiDamageReport = structured_report["structured_response"]
            result = json.loads(structured_report)
            span1.set_outputs(
                    {
                        "pieces_count": len(result.get('pieces', [])),
                        "preview": result,
                    }
                )
            mlflow.log_dict(result, "structured_report.json")

        #===========================
        # Agent2
        #===========================
        with mlflow.start_span("consolidate_output") as span2:
            span2.set_attribute("stage", "agent2")
            formated_prompt2 = prompt2.format(rules_text=RULES_TEXT, liste_text=LIST_TEXT, diagnosis_json=result)
            out2 = agent1.invoke({"messages": formated_prompt2})
            structured_report  = out2["messages"][-1].content
            
            # result:MultiDamageReport = structured_report["structured_response"]
            result = json.loads(structured_report)
            span2.set_outputs(
                    {
                        "pieces_count": len(result.get('pieces', [])),
                        "preview": result,
                    }
                )
            mlflow.log_dict(result, "final_response.json")

    return result


def main(input_transcript:str):
    os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLF_TRACK_URL", "")
    os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLF_USER", "")
    os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLF_TOKEN", "")

    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    
    mlflow.set_experiment(os.getenv("MLF_TRACKING_EXPERIMENT", "price6p_agents_with_mlflow"))
    # the create one agent
    model_name1 = os.getenv("PRICE6_MODEL", "gpt-5-mini")
    agent0 = create_agent(model=ChatOpenAI(model = model_name1))
    # another agent
    model_name2 = os.getenv("PRICE6_MODEL", "gpt-5.4")
    agent1 = create_agent(model=ChatOpenAI(model = model_name2),response_format=MultiDamageReport)
    mlflow.langchain.autolog()  # Enable 1autologging for LangChain
    # load the first prompt
    prompt0:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent0/1"))
    prompt1:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent1/1"))
    prompt2:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent2/1"))

    with mlflow.start_run(run_name="p6p_agents_sg"):
        mlflow.log_params({"model_agent1": model_name1, "model_agent2":model_name2})

        result:MultiDamageReport = inference(agent0, agent1, prompt0, prompt1, prompt2, input_transcript) 

        # here I can Include testing of the "quality" of the result.
        


if __name__ == "__main__":
    load_dotenv(override=True)
    trs = "Conseiller / Expert : Bonjour Monsieur, je vous appelle concernant le dossier de sinistre déclaré le 12 mars. Est-ce que vous pouvez me confirmer l’origine du problème ? Assuré : Oui bonjour. Alors en fait c’est une fuite sous l’évier de la cuisine. Je m’en suis rendu compte parce que ça sentait l’humidité depuis quelques jours. Conseiller : D’accord. Vous savez depuis quand la fuite est présente environ ? Assuré : Je dirais plusieurs jours, peut-être une semaine. C’était une fuite lente, pas un gros dégât d’un coup. Le siphon était fissuré apparemment. Conseiller : Très bien. La fuite était continue ou ponctuelle ? Assuré : Continue oui, ça gouttait tout le temps. Comme c’était sous le meuble, je ne l’ai pas vu tout de suite. Conseiller : Qu’est-ce qui a été touché en premier lieu ? Assuré : Le meuble sous évier a pris toute l’eau. Il est gonflé maintenant, le bois est fichu, on ne peut pas le récupérer. Conseiller : D’accord. Le sol a été impacté également ? Assuré : Oui, j’ai du parquet stratifié dans la cuisine, enfin un sol stratifié. Il a gonflé sur une zone d’environ 3 mètres carrés, avec des taches plus foncées. Conseiller : Est-ce que l’humidité est remontée sur les murs ? Assuré : Oui, le bas du mur derrière le meuble est abîmé, la peinture cloque un peu. Conseiller : Très bien. On est donc bien sur la cuisine. Est-ce qu’il y a d’autres pièces concernées ? Assuré : Oui, malheureusement la salle de bain juste à côté. Le mur commun a pris l’humidité. Conseiller : Pouvez-vous me décrire les dégâts dans la salle de bain ? Assuré : Le mur est humide sur environ 3 mètres carrés. La peinture est encore là mais on voit bien que c’est humide au toucher. Conseiller : Est-ce qu’il y a des moisissures ou des odeurs particulières dans la salle de bain ? Assuré : Pas de moisissure visible pour l’instant, mais une légère odeur d’humidité oui. Conseiller : Très bien. Est-ce que l’eau a coulé au sol dans la salle de bain ? Assuré : Non, pas à ma connaissance. C’est surtout le mur. Conseiller : D’accord. Pour résumer, on a une fuite progressive sous l’évier de la cuisine, due à un siphon fissuré, avec infiltration dans le meuble, le sol stratifié et un mur, puis propagation dans le mur de la salle de bain. C’est bien ça ? Assuré : Oui exactement. Conseiller : Parfait, merci pour ces précisions. Nous allons missionner un artisan pour la suite. Bonne journée Monsieur. Assuré : Merci, bonne journée."
    main(trs)
