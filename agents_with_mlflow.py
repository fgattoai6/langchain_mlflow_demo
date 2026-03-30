
import re
import requests
import mlflow
import json
from dotenv import load_dotenv  

from dataclasses import dataclass, asdict
from typing import List, Optional
from pathlib import Path

import os
from mlflow.entities.model_registry.prompt_version import (
    PromptVersion,
)

gateway_url = os.getenv("PRICE6_GATEWAY_URL", "")
model = os.getenv("PRICE6_MODEL", "")
url = f"{gateway_url.rstrip('/')}/v1/responses"

mlflow.set_tracking_uri("http://localhost:5000")

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "pieces": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "piece": {"type": "string"},
                    "zones": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "zone": {"type": "string"},
                                "travaux": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "properties": {
                                            "lot": {"type": "string"},
                                            "items": {
                                                "type": "array",
                                                "items": {
                                                    "type": "object",
                                                    "additionalProperties": False,
                                                    "properties": {
                                                        "designation": {"type": "string"},
                                                        "description": {"type": "string"},
                                                        "quantite": {"type": "number", "minimum": 0},
                                                        "unite": {"type": "string"},
                                                        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                                                    },
                                                    "required": ["designation", "description", "quantite", "unite", "confidence"],
                                                },
                                            },
                                        },
                                        "required": ["lot", "items"],
                                    },
                                },
                            },
                            "required": ["zone", "travaux"],
                        },
                    },
                },
                "required": ["piece", "zones"],
            },
        },
        # "overall_confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": ["pieces"]#, "confidence"],
}

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class WorkItem:
    designation: str
    description: str
    quantite: float
    unite: str
    confidence: float # can't followed by default valued variable that is unit_price so putting before unit_price
    unit_price: float = 0.0


@dataclass
class LotWork:
    lot: str
    items: List[WorkItem]


@dataclass
class ZoneWork:
    zone: str
    travaux: List[LotWork]


@dataclass
class PieceReport:
    piece: str
    zones: List[ZoneWork]


@dataclass
class MultiDamageReport:
    pieces: List[PieceReport]
    # confidence: float

BASE_DIR = Path(os.getenv("PRICE6_CONFIG_DIR", os.path.dirname(os.path.abspath(__file__))))

def _load_text(name: str) -> str:
    p = BASE_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"Config file not found: {p}")
    with open(p, "r", encoding="utf-8") as f:
        return f.read()




def dict_to_report(data: dict) -> MultiDamageReport:
    pieces_dc: List[PieceReport] = []
    for p in data["pieces"]:
        zones_dc: List[ZoneWork] = []
        for z in p["zones"]:
            travaux_dc: List[LotWork] = []
            for t in z["travaux"]:
                items_dc = []
                for it in t["items"]:
                    # allow extra keys (e.g. unit_price) from asdict
                    item = {k: v for k, v in it.items() if k in ("designation", "description", "quantite", "unite", "unit_price", "confidence")}
                    if "unit_price" not in item:
                        item["unit_price"] = 0.0
                    items_dc.append(WorkItem(**item))
                travaux_dc.append(LotWork(lot=t["lot"], items=items_dc))
            zones_dc.append(ZoneWork(zone=z["zone"], travaux=travaux_dc))
        pieces_dc.append(PieceReport(piece=p["piece"], zones=zones_dc))
    return MultiDamageReport(pieces=pieces_dc) #confidence=data["confidence"])

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

@mlflow.trace
def get_text_response(payload, token):

    resp = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    text = _extract_text(resp.json())
    return text

def main():
    mlflow.set_experiment("agents_with mlflow_test")    

    trs = "[{\"from\":\"user\",\"content\":\"Bonjour j'ai un dégât des eaux\"},{\"from\":\"assistant\",\"content\":\"D'accord, pouvez-vous décrire les pièces concernées ?\"},{\"from\":\"user\",\"content\":\"La cuisine et le salon, environ 30 m²\"}]"
    token = get_llm_token()
    with mlflow.start_run(run_name="mlf_agent_tests"):
       
        prompt:PromptVersion = mlflow.genai.load_prompt(os.getenv("PROMPT_TO_USE", "prompts:/agent0/1"))
        formated_prompt = prompt.format(transcript=trs)
        
        payload = {
             "model": model,
             "input": formated_prompt,
             "temperature": 0,
        }

        text = get_text_response(payload, token)
        
        if not text:
            raise ValueError("Agent0: empty LLM response")

        text = _postprocess(text)

        print("TEXT:", text)

        unit_text = _load_text("unit_allowed.txt")
        liste_text = _load_text("liste.txt")
        prompt1:PromptVersion = mlflow.genai.load_prompt(os.getenv("PROMPT_TO_USE", "prompts:/agent1/1"))
        formated_prompt1 = prompt1.format(unit_text=unit_text, liste_text=liste_text, user_text=text)
        payload1 = {
             "model": model,
             "input": formated_prompt1,
             "temperature": 0,
             "text": {"format": {"type": "json_schema", "name": "multi_damage_report", "strict": True, "schema": SCHEMA}},
        }

        text_json = get_text_response(payload1, token)
        if not text_json:
            raise ValueError("Agent1: empty LLM response")
        data = json.loads(text_json) if isinstance(text_json, str) else text_json
        data = dict_to_report(data)

        # log_text 2 arguments, the second one is to create a file in artifacts 
        mlflow.log_dict(data, "agent1_output.txt")
        mlflow.log_param("model", model)
        mlflow.log_param("prompt_version", prompt.version)
        mlflow.log_param("temperature", 0)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()
