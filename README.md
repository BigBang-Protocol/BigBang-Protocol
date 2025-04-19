![Release](https://img.shields.io/github/v/release/patahul/bigbang-protocol?label=Genesis%20Release&style=flat-square)

# BigBang Protocol

> **Verifiable intent. Enforced policy. Cryptographic governance.**

BigBang Protocol is a post-quantum ready cryptographic trust enforcement layer that transforms every digital action into a **verifiable, policy-bound, tamper-resistant TrustEnvelope**. Designed to replace assumptions with mathematical proof, BigBang ensures that **only authorized actions can occur — and only when policy permits them.**

---

## Features

- **TrustEnvelopes** — signed, structured objects that prove who did what, when, and under what role  
- **Dual-Signature Crypto** — supports both classical (RSA/ECDSA) and post-quantum (Dilithium/Falcon)  
- **TaaS (Trust-as-a-Service)** — real-time policy enforcement engine that validates or blocks actions  
- **Cross-system Auditability** — verify trust even without access to the original system  
- **Envelope Lifecycle** — from creation to archive, actions become legally portable cryptographic objects  

---

## Generate a TrustEnvelope (CLI)

You can create a valid, policy-bound TrustEnvelope using the command-line builder included in this repo:

```bash
python examples/generate_envelope.py \
  --id alice@ministry.gov \
  --role finance.director \
  --action approve_fund_disbursement \
  --method pqc.dilithium3 \
  --scope RM500000
```

---

## Folder Structure

```bash
bigbang-protocol/
├── README.md                # This file
├── LICENSE                  # MIT License
├── ROADMAP.md               # Release goals and plans
├── docs/                    # Concept paper, trust architecture & UIs
├── src/                     # Core signer/verifier logic
├── examples/                # Sample envelopes and builder tool
├── specs/                   # Envelope & Policy JSON schemas
├── assets/images/           # Protocol diagrams & illustrations
├── .github/workflows/       # CI/CD verification flows
```

---

## Release Milestones

- **v1.0.0 – Genesis**  
  Initial TrustEnvelope concept and signer/verifier SDK

- **v1.1.0-alpha – Verifier Engine**  
  TaaS verification API  
  Envelope builder CLI  
  Dockerized verifier service

- **v1.2.0 – Visual Trust + DMS Export**  
  Public Trust Dashboard UI  
  Metadata Viewer (`trust_dms_ui.html`)  
  Export to PDF and JSON  
  GitHub Pages deployment

---

## v1.3.0 – Multi-Signer Envelope Support

BigBang Protocol now supports **quorum-based approval** using multi-actor TrustEnvelopes. This enables workflows such as:

- Maker + Checker approval chains
- Role-based quorum policies
- Verifiable co-signatures with cryptographic enforcement

### New Envelope Structure
- `actors[]`: Multiple identity roles (e.g., finance director, auditor)
- `signatures[]`: Separate signature blocks per actor
- `policy_ref`: Points to a policy requiring multi-role approval

### Sample Files:
- `examples/trust_envelope_v2_multi.json` – Multi-signer envelope
- `specs/sample_trust_policy_v2.json` – Role-based policy rules
- `taas/taas_verifier_multi.py` – TaaS v2 verifier logic

### API Endpoint:
```
POST /verify-envelope-v2/
```

This endpoint validates that all required roles have signed with approved methods.  
Missing or mismatched roles will result in a rejected envelope.

> BigBang v1.3.0 moves beyond trust assumption — into cryptographic quorum enforcement.

---
