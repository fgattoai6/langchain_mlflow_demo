
from langchain.messages import HumanMessage
import mlflow
from langchain.agents import create_agent
from dotenv import load_dotenv  

import os
from mlflow.entities.model_registry.prompt_version import (
    PromptVersion,
)

mlflow.set_tracking_uri("http://localhost:5000")

def main():
    mlflow.set_experiment("langchain_with_mlflow_test")    

    mlflow.langchain.autolog()  # Enable autologging for LangChain
    
    
    with mlflow.start_run(run_name="agent_demo"):
        agent = create_agent(
            model="gpt-5",
        )
       
        prompt:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/test_agent1/2"))
        formated_prompt = prompt.format(city="Paris")
        
        response = agent.invoke({"messages": formated_prompt})
        print(response)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()
