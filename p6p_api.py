import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

    yield

    logger.info("App shutting down")


app = FastAPI(lifespan=lifespan)


# input description of the api. keep input "easy" to handle; no complicated/nested JSON. 
class Transcript(BaseModel):
    content: str

@app.post("/transcript_to_quotation", response_model=None) # TODO, we need a pydantic model to define the input/output of the api
async def ingest(request: Transcript): 
    logger.info("Received payload")

    # TODO call the "wrapped" function here (see the other file )
    return {"received": request.content}

    # in case you return error, use this line; and write proper detail static text (no formating)
    # raise HTTPException(status_code=400, detail=".....")