
import os
import mlflow
from dotenv import load_dotenv  
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from mlflow.entities.model_registry.prompt_version import (
    PromptVersion,
)
from schemas.damage_report_eng import MultiDamageReport
def main(input_transcript:str):
    mlflow.set_experiment(os.getenv("MLF_TRACKING_EXPERIMENT", "langchain_with_mlflow_test"))

    chat_model = ChatOpenAI(model = os.getenv("PRICE6_MODEL", "gpt-5-mini") )
    # the create one agent
    agent = create_agent(model=chat_model)
    agent2 = create_agent(model=chat_model,response_format=MultiDamageReport)
    mlflow.langchain.autolog()  # Enable 1autologging for LangChain
    # load the first prompt
    prompt:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent0/1"))

    with mlflow.start_run(run_name="p6p_agents"):
        with mlflow.start_span("p6p") as allrunspan:
            allrunspan.set_attribute("input_transcript", str(input_transcript))
            with mlflow.start_span("semantic_alignment") as span1:
                
                formated_prompt = prompt.format(transcript=input_transcript)
                response = agent.invoke({"messages": formated_prompt})
                response_text = response["messages"][-1].content
                mlflow.log_text(response_text, "semantic_alignment.json")

            with mlflow.start_span("structured_output") as span2:
                result = agent2.invoke({
                    "messages": [{"role": "user", "content": f"Extract contact info from: {response_text}"}] #probeably we don't need a mlf prompt here
                })
                result:MultiDamageReport = result["structured_response"]
                mlflow.log_text(str(result), "result2.txt")

if __name__ == "__main__":
    load_dotenv(override=True)
    trs = "[{\"from\":\"user\",\"content\":\"Bonjour j'ai un dégât des eaux\"},{\"from\":\"assistant\",\"content\":\"D'accord, pouvez-vous décrire les pièces concernées ?\"},{\"from\":\"user\",\"content\":\"La cuisine et le salon, environ 30 m²\"}]"
    main(trs)
