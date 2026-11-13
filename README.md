# GENAI Summit — Hackathon Starter

A lightweight **FastAPI (Python)** + **Next.js (React)** starter template built around the core hackathon pattern:

> **Goal → Plan → Tool Execution → End-to-End Deliverable**

---

## Project Structure

```text
Gen-AI-Summit/
├── .github/workflows/ci.yml # GitHub Actions CI (Ruff, Pytest, Prettier, Typecheck, Next build)
├── backend/
│   ├── main.py              # FastAPI endpoints (/api/health, /api/agent/run)
│   └── agent.py             # High-level ProactiveAgent loop + generic tool registry
├── frontend/
│   └── src/app/page.tsx     # Minimal Next.js UI for running goals and viewing steps
├── tests/
│   └── test_api.py          # FastAPI smoke tests
├── .env.example             # Environment variable template
├── .prettierrc              # Shared Prettier formatting rules
├── pyproject.toml           # Python dependencies & Ruff/Pytest config (managed via uv)
└── run.ps1                  # Quick backend launcher for Windows
```

---

## Quickstart

### 1. Run Backend (FastAPI + `uv`)

```powershell
.\run.ps1
# Or manually:
uv run uvicorn backend.main:app --reload --port 8000
```

* API: `http://localhost:8000`
* Interactive Swagger Docs: `http://localhost:8000/docs`

### 2. Run Frontend (Next.js)

```powershell
cd frontend
npm install
npm run dev
```

* Web UI: `http://localhost:3000`

---

## Checks & CI

* **Backend lint & tests:**
  ```powershell
  uv run ruff check .
  uv run pytest -v
  ```
* **Frontend format, typecheck & build:**
  ```powershell
  cd frontend
  npm run format        # auto-format with Prettier
  npm run format:check  # verify formatting
  npm run typecheck
  npm run build
  ```

---

## How to Customize Tomorrow

1. **Add your API keys** in `.env` (copied from `.env.example`).
2. **Add tools** in `backend/agent.py` inside the `TOOLS` dictionary.
3. **Wire your LLM** into `ProactiveAgent.run()` in `backend/agent.py`.
