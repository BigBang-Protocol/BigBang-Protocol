# BigBang TaaS Verifier — Deployment Guide

This guide provides step-by-step instructions for deploying the TaaS (Trust-as-a-Service) Verifier component of the BigBang Protocol. It supports both local development and Docker-based deployments.

---

## Option 1: Run Locally (Python)

### 1. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 2. Run the verifier API

```bash
python taas_verifier_api.py
```

### 3. Access the API

Open your browser:
```
http://localhost:8000/docs
```

You can use the Swagger UI to test the `/verify-envelope/` endpoint.

---

## Option 2: Run via Docker

### 1. Build the Docker image

```bash
docker build -t bigbang-taas-api .
```

### 2. Run the Docker container

```bash
docker run -p 8000:8000 bigbang-taas-api
```

This will expose the verifier API at:
```
http://localhost:8000/verify-envelope
```

---

## (Optional) Expose to Public via Ngrok

If you're testing remotely or want to simulate a public server:

```bash
ngrok http 8000
```

This will give you a public HTTPS link like:
```
https://abc123.ngrok.io/verify-envelope
```

You can use this URL for:
- GitHub Actions CI testing
- Partner integrations
- Remote validator testing

---

## Files Required

Ensure the following are in your working directory:
- `taas_verifier_api.py`
- `sample_trust_policy.json`
- `requirements.txt`
- `Dockerfile`

---

## Questions or Contributions

Visit the GitHub repository:  
[github.com/bigbang-protocol/bigbang-protocol](https://github.com/your-username/bigbang-protocol)
