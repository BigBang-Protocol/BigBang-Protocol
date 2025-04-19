import json

with open("test_envelope.json") as f:
    envelope = json.load(f)

with open("../specs/sample_trust_policy.json") as f:
    policy = json.load(f)

actor_role = envelope["actor"]["role"]
intent = envelope["intent"]["action"]
method_used = envelope["actor"]["method"]
scope = envelope["intent"]["scope"]

matched = False
for rule in policy["rules"]:
    if (
        rule["role"] == actor_role and
        rule["action"] == intent and
        method_used in rule["method"]
    ):
        print("✅ Envelope is policy-compliant")
        matched = True
        break

if not matched:
    print("❌ Envelope rejected by policy")
