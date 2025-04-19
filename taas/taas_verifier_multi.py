from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()

class Actor(BaseModel):
    id: str
    role: str
    device_id: Optional[str] = None
    method: str

class Intent(BaseModel):
    action: str
    scope: Optional[str] = None
    target_hash: Optional[str] = None

class Signature(BaseModel):
    actor_id: str
    pqc: Optional[str] = None
    classical: Optional[str] = None

class Envelope(BaseModel):
    envelope_id: str
    actors: List[Actor]
    intent: Intent
    policy_ref: str
    timestamp: str
    signatures: List[Signature]

@app.post("/verify-envelope-v2/")
def verify_multi_signer_envelope(envelope: Envelope):
    try:
        with open("sample_trust_policy_v2.json", "r") as f:
            policy = json.load(f)
    except Exception:
        raise HTTPException(status_code=500, detail="Policy file not found")

    required_roles = set(rule["role"] for rule in policy.get("rules", []))
    signed_roles = set()

    for sig in envelope.signatures:
        actor = next((a for a in envelope.actors if a.id == sig.actor_id), None)
        if actor:
            for rule in policy["rules"]:
                if rule["role"] == actor.role and envelope.intent.action == rule["action"]:
                    if actor.method in rule["method"]:
                        signed_roles.add(actor.role)

    if required_roles.issubset(signed_roles):
        return {
            "status": "valid",
            "message": "✅ All required roles signed with compliant methods.",
            "envelope_id": envelope.envelope_id
        }

    return {
        "status": "rejected",
        "message": f"❌ Required roles not fulfilled. Missing: {required_roles - signed_roles}",
        "envelope_id": envelope.envelope_id
    }