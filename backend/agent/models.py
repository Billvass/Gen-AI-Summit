from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


TrackType = Literal["auto", "enterprise_voice", "biotech", "creative_fal", "open_hardware"]


class GoalRequest(BaseModel):
    goal: str = Field(..., min_length=3, description="High-level objective for the agent to execute end-to-end")
    track: TrackType = Field(default="auto", description="Hackathon track preset or 'auto' to auto-detect")
    max_steps: int = Field(default=5, ge=1, le=10, description="Maximum autonomous tool-calling iterations")
    context: Optional[Dict[str, Any]] = Field(default=None, description="Optional structured context or parameters")


class PlanStep(BaseModel):
    step_number: int
    title: str
    tool_name: str
    rationale: str
    status: Literal["pending", "running", "completed", "failed"] = "pending"


class DeliverableArtifact(BaseModel):
    title: str
    artifact_type: Literal["markdown", "json", "image", "action_receipt", "biotech_dossier"]
    content: Any
    summary: str


class AgentRunResult(BaseModel):
    goal: str
    detected_track: str
    plan: List[PlanStep]
    tool_traces: List[Dict[str, Any]]
    deliverable: DeliverableArtifact
    proactive_next_actions: List[str]
    execution_mode: str


class ApiKeyUpdateRequest(BaseModel):
    keys: Dict[str, str]
