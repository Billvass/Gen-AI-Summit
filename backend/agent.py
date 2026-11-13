from typing import Callable, Dict, List
from pydantic import BaseModel


class StepResult(BaseModel):
    step: int
    action: str
    tool: str
    output: str


class AgentResponse(BaseModel):
    goal: str
    plan: List[str]
    steps: List[StepResult]
    deliverable: str


# ---------------------------------------------------------------------------
# Generic Tool Registry — add or replace tools here tomorrow once the
# specific challenge is announced.
# ---------------------------------------------------------------------------
def search_tool(query: str) -> str:
    """Placeholder for web/data lookup."""
    return f"Fetched context for: '{query}'"


def analyze_tool(data: str) -> str:
    """Placeholder for processing or reasoning over data."""
    return f"Analyzed key patterns from: {data}"


def action_tool(payload: str) -> str:
    """Placeholder for taking an external action (API call, webhook, generation)."""
    return f"Executed action with: {payload}"


TOOLS: Dict[str, Callable[[str], str]] = {
    "search": search_tool,
    "analyze": analyze_tool,
    "act": action_tool,
}


# ---------------------------------------------------------------------------
# High-Level Proactive Agent Loop: Goal -> Plan -> Execute Tools -> Deliver
# ---------------------------------------------------------------------------
class ProactiveAgent:
    async def run(self, goal: str) -> AgentResponse:
        # 1. Plan: Break the high-level goal into concrete steps
        plan = [
            f"Gather information needed for: {goal}",
            "Analyze findings and determine best action",
            "Execute end-to-end action and package deliverable",
        ]

        # 2. Execute: Run tools for each step
        steps: List[StepResult] = [
            StepResult(step=1, action=plan[0], tool="search", output=TOOLS["search"](goal)),
            StepResult(step=2, action=plan[1], tool="analyze", output=TOOLS["analyze"](goal)),
            StepResult(step=3, action=plan[2], tool="act", output=TOOLS["act"](goal)),
        ]

        # 3. Deliver: Synthesize final end-to-end result
        deliverable = (
            f"Completed goal: '{goal}'\n\n"
            + "\n".join(f"- Step {s.step} ({s.tool}): {s.output}" for s in steps)
        )

        return AgentResponse(
            goal=goal,
            plan=plan,
            steps=steps,
            deliverable=deliverable,
        )


agent = ProactiveAgent()
