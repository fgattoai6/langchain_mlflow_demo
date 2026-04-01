import logging
from contextlib import asynccontextmanager
import os, dotenv

from fastapi import FastAPI, HTTPException
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import mlflow
from pydantic import BaseModel

from agent_with_lc_mlf_oai import inference
from schemas.damage_report_fr import MultiDamageReport

def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("App starting up")

    # initialize shared resources here
    # mlflow.set_experiment(os.getenv("MLF_TRACKING_EXPERIMENT", "langchain_with_mlflow_test"))
    os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLF_TRACK_URL", "")
    os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLF_USER", "")
    os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLF_TOKEN", "")

    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    
    mlflow.set_experiment(os.getenv("MLF_TRACKING_EXPERIMENT", "price6p_agents_api"))

    mlflow.langchain.autolog()  # Enable 1autologging for LangChain

    yield

    logger.info("App shutting down")


app = FastAPI(lifespan=lifespan)


# input description of the api. keep input "easy" to handle; no complicated/nested JSON. 
# POST request body validation via Pydantic BaseModel, that it should always be a string.
class Transcript(BaseModel):
    transcript: str

@app.post("/transcript_to_quotation", ) 
async def ingest(request: Transcript) ->MultiDamageReport: 
    logger.info("Received payload")
    # the create one agent
    model_name1 = os.getenv("PRICE6_MODEL", "gpt-5-mini")
    agent0 = create_agent(model=ChatOpenAI(model = model_name1))

    # another agent
    model_name2 = os.getenv("PRICE6_MODEL", "gpt-5.4")
    agent1 = create_agent(model=ChatOpenAI(model = model_name2),response_format=MultiDamageReport)
    
    prompt0 = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent0/1"))
    prompt1 = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent1/1"))
    prompt2 = mlflow.genai.load_prompt( os.getenv("PROMPT_TO_USE", "prompts:/price6p_agent2/1"))

    mlflow.start_run(run_name="api_transcript_to_quotation")
    try:
        result:MultiDamageReport = inference(agent0, agent1, prompt0, prompt1, prompt2, request.transcript) 
        return result
    finally:
        mlflow.end_run()
    # in case you return error, use this line; and write proper detail static text (no formating)
    # raise HTTPException(status_code=400, detail=".....")

if __name__ == "__main__":
    import uvicorn
    dotenv.load_dotenv()
    uvicorn.run("p6p_api:app", host="0.0.0.0", port=8000, reload=True)