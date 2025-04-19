from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()

class Actor(BaseModel):
    id: str
    role: str
    method: str

class Intent(BaseModel):
    action: str
    scope: Optional[str] = None
    target_hash: Optional[str] = None

class Signatures(BaseModel):
    pqc: str
    classical: str

class Envelope(BaseModel):
    envelope_id: str
    actor: Actor
    intent: Intent
    policy_ref: str
    timestamp: str
    signatures: Signatures

@app.post("/verify-envelope/")
def verify_envelope(envelope: Envelope):
    try:
        with open("sample_trust_policy.json", "r") as f:
            policy = json.load(f)
    except Exception:
        raise HTTPException(status_code=500, detail="Policy file not found")

    for rule in policy.get("rules", []):
        if (
            rule["role"] == envelope.actor.role and
            rule["action"] == envelope.intent.action and
            envelope.actor.method in rule["method"]
        ):
            return {
                "status": "valid",
                "message": "â Envelope is policy-compliant",
                "envelope_id": envelope.envelope_id
            }

    return {
        "status": "rejected",
        "message": "â Envelope rejected: policy mismatch",
        "envelope_id": envelope.envelope_id
    }
