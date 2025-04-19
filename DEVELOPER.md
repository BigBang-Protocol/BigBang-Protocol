# BigBang Protocol — Developer Guide

This guide provides technical documentation for developers integrating or contributing to BigBang Protocol. It includes signing, verifying, TrustEnvelope format, TaaS API usage, and policy enforcement mechanics.

---

## 1. TrustEnvelope Structure (JSON)

A TrustEnvelope is a tamper-proof object that contains:

```json
{
  "id": "alice@ministry.gov",
  "role": "finance.director",
  "action": "approve_fund_disbursement",
  "timestamp": "2025-04-20T12:34:56Z",
  "signature_classical": "<RSA/ECDSA-SIGNATURE>",
  "signature_pqc": "<Dilithium/Falcon-SIGNATURE>",
  "policy_hash": "<SHA3-512>",
  "scope": "RM500000"
}
```

---

## 2. Signing an Envelope (CLI)

Use the CLI to generate an envelope from any approved action:

```bash
python examples/generate_envelope.py \
  --id alice@ministry.gov \
  --role finance.director \
  --action approve_fund_disbursement \
  --method pqc.dilithium3 \
  --scope RM500000
```

Supported methods: `rsa`, `ecdsa`, `pqc.dilithium2`, `pqc.dilithium3`, `pqc.falcon`

---

## 3. Verifying an Envelope (CLI)

Use the verifier script to validate signatures and policy compliance:

```bash
python src/verify.py --envelope path/to/envelope.json
```

Returns:

- `✅ Signature Valid`
- `❌ Signature Invalid or Policy Breach`

---

## 4. Trust-as-a-Service (TaaS) API

### POST `/verify-envelope`

Request Body:
```json
{
  "envelope": { ... },
  "policy": { ... }
}
```

Response:
```json
{
  "valid": true,
  "score": 98,
  "logs": [
    "Signature verified",
    "Policy matched for role: finance.director"
  ]
}
```

---

## 5. Policy Example

```json
{
  "allowed_roles": ["finance.director", "cfo"],
  "allowed_actions": ["approve_fund_disbursement"],
  "max_amount": "RM1000000"
}
```

---

## 6. Envelope Lifecycle

1. **Created** — Action initiated and signed
2. **Verified** — Cross-checked against policies
3. **Archived** — Stored or transmitted with audit metadata
4. **Anchored** *(optional)* — Hash written to blockchain or IPFS

---

## 7. Federation & Multi-Signer

Multi-party signing is supported:

```json
{
  "signers": [
    { "id": "ceo@org.com", "signature": "<...>" },
    { "id": "cfo@org.com", "signature": "<...>" }
  ],
  "quorum": 2
}
```

Use the `trust_dashboard_multi_v3.html` UI or CLI to collect required signers.

---

## 8. Directory Overview

```
bigbang-protocol/
├── src/                # Verifier, signer, utils
├── examples/           # CLI builders
├── specs/              # Envelope schema, policy schema
├── taas/               # Flask API for TaaS
├── docs/               # GitHub Pages frontend
├── assets/images/      # Architecture diagrams
```

---

## 9. License & Contribution

BigBang Protocol is licensed under **MIT**.

Contributions welcome via:
- Issues
- Pull requests
- Forked integrations for ERP, DMS, or national CA tools

> Contact: [patahul@outlook.com](mailto:patahul@outlook.com) · GitHub: [bigbang-protocol](https://github.com/bigbang-protocol)