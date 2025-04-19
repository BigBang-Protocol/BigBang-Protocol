import json
import uuid
from datetime import datetime

def generate_envelope(actor_id, role, action, method, scope="RM100000"):
    envelope = {
        "envelope_id": str(uuid.uuid4()),
        "actor": {
            "id": actor_id,
            "role": role,
            "device_id": "device-001",
            "method": method
        },
        "intent": {
            "action": action,
            "scope": scope,
            "target_hash": "SHA256:demo0000000000000000000000000000"
        },
        "policy_ref": "trustpolicy-v1.0.0-hash123",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "signatures": {
            "pqc": "BASE64_PQC_SIGNATURE_PLACEHOLDER",
            "classical": "BASE64_RSA_SIGNATURE_PLACEHOLDER"
        }
    }

    filename = f"generated_envelope_{envelope['envelope_id']}.json"
    with open(filename, "w") as f:
        json.dump(envelope, f, indent=2)

    print(f"✅ Envelope generated and saved to {filename}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a TrustEnvelope")
    parser.add_argument("--id", required=True, help="Actor ID (e.g. alice@org.com)")
    parser.add_argument("--role", required=True, help="Actor role")
    parser.add_argument("--action", required=True, help="Intent action (e.g. approve_fund)")
    parser.add_argument("--method", default="pqc.dilithium3", help="Signature method")
    parser.add_argument("--scope", default="RM100000", help="Scope or amount involved")

    args = parser.parse_args()
    generate_envelope(args.id, args.role, args.action, args.method, args.scope)