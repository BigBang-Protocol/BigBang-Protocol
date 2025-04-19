# BigBang Protocol — Roadmap

This roadmap outlines the core development milestones of the BigBang Protocol from Genesis to full cross-sector cryptographic governance infrastructure.

---

✅ **v1.0.0 — Genesis Release (April 2025)**
- TrustEnvelope schema (dual-signature + metadata)
- Sample TrustPolicy logic
- Python verifier prototype (verify.py)
- GitHub Actions test automation
- GitHub Pages homepage
- MIT-licensed public release

---

✅ **v1.1.0 — TaaS Alpha + Envelope Builder**
- REST API for TaaS verifier (FastAPI)
- Envelope Builder CLI (generate_envelope.py)
- Policy Enforcement Middleware
- Expanded role-based policy schema
- Real-time audit logging (stubbed)
- CI: Envelope expiration + policy hash validation

---

✅ **v1.2.0 — Visual Trust Dashboards + DMS Integration**
- Web-based verifier dashboard (HTML/JS)
- Upload + validate envelopes via browser
- Envelope viewer with metadata & signature check
- Downloadable trust reports (PDF/JSON)
- Public GitHub Pages UI deployment

---

✅ **v1.3.0 — Governance Federation & Quorum Support**
- Multi-signer envelope flow (CEO + CFO + Auditor)
- Quorum-based approval envelopes (via TrustPolicy v2)
- Cross-org envelope verification logic
- Chain-of-Trust simulation (step-by-step signing)
- Trust report export with full envelope metadata

> *Optional blockchain/IPFS anchoring has been deferred to v1.4.0 and beyond.*

---

🧭 **Suggested v1.4.0 — Federation Anchoring & Delegation**
- Blockchain / IPFS anchoring of envelope hash
- TrustEnvelope anchoring registry (optional cross-verifier lookup)
- Delegated signer logic (e.g., assistant to CFO)
- DID + identity-binding envelope logic
- Verifiable revocation status

---

**Trust is no longer assumed.  
It is signed, policy-bound, and mathematically enforced.**
