from typing import Dict, List

BASE_PROACTIVE_SYSTEM_PROMPT = """You are an autonomous, proactive end-to-end AI Agent built for the GENAI Summit Hackathon.
Your mission:
1. Take a high-level goal from the user.
2. Figure out everything that needs to happen without hand-holding.
3. Proactively invoke the available tools (web scraping via Firecrawl, Biotech databases, fal.ai media generation, Enterprise/Voice workflows via Wonderful, and code/hardware sandboxes via boxd).
4. Verify your findings and produce a concrete, actionable end-to-end deliverable (not just a chat reply).
5. Always include 2-3 proactive follow-up actions you have either already prepared or recommend executing next.
"""

TRACK_PROMPTS: Dict[str, str] = {
    "auto": BASE_PROACTIVE_SYSTEM_PROMPT,
    "enterprise_voice": (
        BASE_PROACTIVE_SYSTEM_PROMPT
        + "\nTRACK FOCUS: Voice & Enterprise Agents (with Wonderful).\n"
        "Prioritize customer/enterprise context gathering, policy verification, CRM/ticket execution, "
        "and generating structured voice-ready scripts and enterprise webhook actions."
    ),
    "biotech": (
        BASE_PROACTIVE_SYSTEM_PROMPT
        + "\nTRACK FOCUS: Biotech & AI (with Athens LifeTech Park).\n"
        "Prioritize querying real biological databases (UniProt proteins, ChEMBL bioactive compounds, "
        "OpenTargets disease associations), running quantitative molecular checks in the sandbox, and "
        "producing structured target/lead dossiers."
    ),
    "creative_fal": (
        BASE_PROACTIVE_SYSTEM_PROMPT
        + "\nTRACK FOCUS: Content & Digital Art (with fal).\n"
        "Prioritize researching visual/brand references, crafting rich multi-shot prompts, generating "
        "visual assets via fal.ai, and assembling a complete creative campaign deliverable."
    ),
    "open_hardware": (
        BASE_PROACTIVE_SYSTEM_PROMPT
        + "\nTRACK FOCUS: Open Track & Hardware Integration.\n"
        "Prioritize combining external telemetry/research, executing quantitative control logic in the sandbox, "
        "and dispatching real-time hardware/IoT actuator commands or webhook payloads."
    ),
}

TRACK_PRESETS: List[Dict[str, str]] = [
    {
        "id": "biotech_egfr",
        "track": "biotech",
        "label": "Biotech & AI (Athens LifeTech Park)",
        "badge": "Live Bio APIs",
        "goal": "Investigate human EGFR (UniProt P00533) as an oncology target, fetch its top bioactive inhibitors from ChEMBL, compute molecular weight/lipophilicity statistics, and compile a target validation dossier.",
    },
    {
        "id": "enterprise_wonderful",
        "track": "enterprise_voice",
        "label": "Voice & Enterprise (Wonderful)",
        "badge": "Enterprise Agent",
        "goal": "Research a company's public pricing/SLA page, diagnose a VIP customer escalation for delayed shipment #ORD-9842, trigger a proactive resolution workflow with SLA credit, and prepare a natural voice call script.",
    },
    {
        "id": "creative_fal_campaign",
        "track": "creative_fal",
        "label": "Content & Digital Art (fal)",
        "badge": "Generative Media",
        "goal": "Design an interactive product launch campaign for an eco-tech wearable in Athens: research Mediterranean futuristic aesthetics, generate hero concept art via fal.ai, and produce a multi-channel creative brief.",
    },
    {
        "id": "open_hardware_agent",
        "track": "open_hardware",
        "label": "Open Track + Hardware",
        "badge": "Edge / IoT Ready",
        "goal": "Analyze simulated cold-chain bioreactor telemetry anomalies (temp spike to 11.4C), calculate thermal drift trajectory in Python sandbox, and dispatch an emergency cooling actuator command + incident report.",
    },
]
