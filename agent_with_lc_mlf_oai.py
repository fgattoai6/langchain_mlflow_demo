
import os
import mlflow
from dotenv import load_dotenv  
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from mlflow.entities.model_registry.prompt_version import PromptVersion
from schemas.damage_report_eng import MultiDamageReport


def main(input_transcript:str):
    mlflow.set_experiment(os.getenv("MLF_TRACKING_EXPERIMENT", "langchain_with_mlflow_test"))
    # the create one agent
    model_name1 = os.getenv("PRICE6_MODEL", "gpt-5-mini")
    agent = create_agent(model=ChatOpenAI(model = model_name1))
    # another agent
    model_name2 = os.getenv("PRICE6_MODEL", "gpt-5.4")
    agent2 = create_agent(model=ChatOpenAI(model = model_name2),response_format=MultiDamageReport)
    mlflow.langchain.autolog()  # Enable 1autologging for LangChain
    # load the first prompt
    prompt:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent0/1"))

    with mlflow.start_run(run_name="p6p_agents"):
        mlflow.log_params({"model_agent1": model_name1, "model_agent2":model_name2})

        # key "function" input is ~here. not before, not after (I keep tracing but  reject the run)
        with mlflow.start_span("p6p", attributes={"input_transcript":str(input_transcript) }) as allrunspan:
            with mlflow.start_span("semantic_alignment") as span1:
                formated_prompt = prompt.format(transcript=input_transcript)
                response = agent.invoke({"messages": formated_prompt})
                response_text = response["messages"][-1].content
                mlflow.log_text(response_text, "semantic_alignment.json")

            with mlflow.start_span("structured_output") as span2:
                result = agent2.invoke({
                    "messages": [{"role": "user", "content": f"Extrait les dégats constaté dans la description suivante: \n{response_text}"}] 
                })
                result:MultiDamageReport = result["structured_response"]
                mlflow.log_text(str(result), "result2.txt")
            # TODO add the final agen step bellow
            with mlflow.start_span("consolidate_output"):
                ...
        # end of the tracing
        # TODO key function return here; not before nor after. exactly here. 

        # here I can Include testing of the "quality" of the result.
        


if __name__ == "__main__":
    load_dotenv(override=True)
    trs = "[{\"from\":\"user\",\"content\":\"Bonjour j'ai un dégât des eaux\"},{\"from\":\"assistant\",\"content\":\"D'accord, pouvez-vous décrire les pièces concernées ?\"},{\"from\":\"user\",\"content\":\"La cuisine et le salon, environ 30 m²\"}]"
    main(trs)
