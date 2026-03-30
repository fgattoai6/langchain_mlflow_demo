
import re
import os
import requests
import json
import mlflow
from dotenv import load_dotenv  

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from mlflow.entities.model_registry.prompt_version import (
    PromptVersion,
)

from agents_with_mlflow import MultiDamageReport
def main():
    print("start ...")
    print(os.getenv("MLFLOW_TRACKING_URI"))
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

    print("set_exp.txt")
    mlflow.set_experiment("langchain_with_mlflow_test")    
    model = os.getenv("PRICE6_MODEL", "chat-gpt5-mini")
    
    # print("TOKEN:", token, "URL:", url)

    
    trs = "[{\"from\":\"user\",\"content\":\"Bonjour j'ai un dégât des eaux\"},{\"from\":\"assistant\",\"content\":\"D'accord, pouvez-vous décrire les pièces concernées ?\"},{\"from\":\"user\",\"content\":\"La cuisine et le salon, environ 30 m²\"}]"
    print("trs ...")
    #first create the LLM connection object
    chat_model = ChatOpenAI(
        model = "gpt-5-mini", #"gpt-4-turbo",
    )
    print("creating agent...")
    # the create one agent
    agent = create_agent(
        model=chat_model,
    )
    agent2 = create_agent(
        model="gpt-5",
        response_format=MultiDamageReport  # Auto-selects ProviderStrategy
    )
    mlflow.langchain.autolog()  # Enable autologging for LangChain
    # load the prompt 
    print("running ...")
    with mlflow.start_run(run_name="p6_plus_agents"):
        with mlflow.start_span("p6_plus") as allrunspan:
            allrunspan.set_attribute("input_transcript", str(trs))
            with mlflow.start_span("semantic_alignment") as span1:
                print("check1 ...")
                prompt:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent0/1"))
                formated_prompt = prompt.format(transcript=trs)
                
                response = agent.invoke({"messages": formated_prompt})
                response_text = response["messages"][-1].content

                
                # log_text 2 arguments, the second one is to create a file in ar tifacts 
                mlflow.log_text(response_text, "conversation.json")
            print("step1 done!")
            with mlflow.start_span("structured_output") as span2:
                print("check2 ...")
                result = agent2.invoke({
                    "messages": [{"role": "user", "content": f"Extract contact info from: {response_text}"}]
                })

                result:MultiDamageReport = result["structured_response"]
                mlflow.log_text(str(result), "result2.txt")
                


if __name__ == "__main__":
    load_dotenv(override=True)  # Load environment variables from .env file
    main()
