
import re
import os
import requests
import mlflow
from dotenv import load_dotenv  

# from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from mlflow.entities.model_registry.prompt_version import (
    PromptVersion,
)

mlflow.set_tracking_uri("http://localhost:5000")

def _extract_text(data: dict) -> str:
    text = ""
    if "choices" in data and data["choices"]:
        text = data["choices"][0].get("message", {}).get("content") or ""
    if "output" in data and data["output"]:
        out = data["output"][0]
        content = out.get("content") or []
        if content and isinstance(content[0].get("text"), str):
            text = content[0]["text"]
    return text or ""

def _postprocess(text: str) -> str:
        text = text.replace("\r\n", "\n").strip() + "\n"
        text = re.sub(r"^\s*[•·]\s*", "\t\t- ", text, flags=re.MULTILINE)
        text = re.sub(r"^-\s*", "\t\t- ", text, flags=re.MULTILINE)
        return text

def get_llm_token() -> str:
    token_url = os.getenv("PRICE6_TOKEN_URL", "")
    client_id = os.getenv("PRICE6_CLIENT_ID", "")
    client_secret = os.getenv("PRICE6_CLIENT_SECRET", "")
    payload = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
    resp = requests.post(
        token_url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]

def main():
    gateway_url = os.getenv("PRICE6_GATEWAY_URL", "")
    model = os.getenv("PRICE6_MODEL", "chat-gpt5-mini")
    url = f"{gateway_url.rstrip('/')}/v1/responses"
    token = get_llm_token()

    # print("TOKEN:", token, "URL:", url)
    mlflow.set_experiment("langchain_with_mlflow_test")    

    mlflow.langchain.autolog()  # Enable autologging for LangChain
    
    trs = "[{\"from\":\"user\",\"content\":\"Bonjour j'ai un dégât des eaux\"},{\"from\":\"assistant\",\"content\":\"D'accord, pouvez-vous décrire les pièces concernées ?\"},{\"from\":\"user\",\"content\":\"La cuisine et le salon, environ 30 m²\"}]"

    with mlflow.start_run(run_name="agent_tests"):
        # agent = create_agent(
        #     model="gpt-5-mini",
        # )
        import httpx

        client = httpx.Client(
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
        )

        agent = ChatOpenAI(
            model = model, #"gpt-4-turbo",
            openai_api_base=url,
            # openai_api_key=os.getenv('OPENAI_API_KEY', ""),
            # http_client=client
            default_headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        prompt:PromptVersion = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/Agent1/2"))
        formated_prompt = prompt.format(transcript=trs)
        
        print("formatted prompt::", formated_prompt)
        # response = agent.invoke({"messages": formated_prompt})
        response = agent.invoke(formated_prompt)
        print("RES:::", response)
        # text = _extract_text(response)
        text = _postprocess(response.content)

        print("TEXT:", text)
        # log_text 2 arguments, the second one is to create a file in artifacts 
        mlflow.log_text(text, "agent0_output.txt")

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()
