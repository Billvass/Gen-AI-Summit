from typing import Any, Callable, Dict, List
from backend.tools.biotech_tool import biotech_target_lookup
from backend.tools.enterprise_tool import enterprise_voice_action
from backend.tools.fal_tool import generate_media_fal
from backend.tools.firecrawl_tool import web_scrape_firecrawl
from backend.tools.sandbox_tool import run_sandbox_analysis


TOOL_CATALOG: List[Dict[str, Any]] = [
    {
        "name": "web_scrape_firecrawl",
        "sponsor": "Firecrawl",
        "track": "All Tracks",
        "description": "Scrapes web URLs or researches domain topics into LLM-ready markdown.",
    },
    {
        "name": "biotech_target_lookup",
        "sponsor": "Athens LifeTech Park (UniProt / ChEMBL / AlphaFold)",
        "track": "Biotech & AI",
        "description": "Fetches live protein targets, AlphaFold 3D coordinates, and ChEMBL small-molecule inhibitors.",
    },
    {
        "name": "generate_media_fal",
        "sponsor": "fal.ai",
        "track": "Content & Digital Art",
        "description": "Generates concept art, campaign visuals, and digital media via fal.ai models.",
    },
    {
        "name": "enterprise_voice_action",
        "sponsor": "Wonderful",
        "track": "Voice & Enterprise Agents",
        "description": "Executes proactive CRM/SLA resolutions and synthesizes SSML voice agent scripts.",
    },
    {
        "name": "run_sandbox_analysis",
        "sponsor": "boxd / Open Track Hardware",
        "track": "Open Track & All Tracks",
        "description": "Runs isolated numerical/statistical analysis in a sandbox and dispatches optional hardware commands.",
    },
]

TOOL_HANDLERS: Dict[str, Callable[..., Any]] = {
    "web_scrape_firecrawl": web_scrape_firecrawl,
    "biotech_target_lookup": biotech_target_lookup,
    "generate_media_fal": generate_media_fal,
    "enterprise_voice_action": enterprise_voice_action,
    "run_sandbox_analysis": run_sandbox_analysis,
}


async def execute_tool(tool_name: str, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    handler = TOOL_HANDLERS.get(tool_name)
    if not handler:
        return {"error": f"Unknown tool: {tool_name}"}
    return await handler(**kwargs)
