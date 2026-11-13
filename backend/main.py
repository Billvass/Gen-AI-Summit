from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.agent import AgentResponse, TOOLS, agent

load_dotenv()

app = FastAPI(title="GENAI Summit Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GoalInput(BaseModel):
    goal: str


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "available_tools": list(TOOLS.keys()),
    }


@app.post("/api/agent/run", response_model=AgentResponse)
async def run_agent(payload: GoalInput):
    return await agent.run(payload.goal)
