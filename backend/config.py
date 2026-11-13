import os
from typing import Dict
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Dynamic settings manager supporting .env and live runtime overrides."""

    def __init__(self) -> None:
        self._overrides: Dict[str, str] = {}

    def get(self, key: str, default: str = "") -> str:
        if key in self._overrides and self._overrides[key]:
            return self._overrides[key]
        return os.getenv(key, default).strip()

    def set_override(self, key: str, value: str) -> None:
        if value and value.strip():
            self._overrides[key] = value.strip()
        elif key in self._overrides:
            del self._overrides[key]

    @property
    def gemini_api_key(self) -> str:
        return self.get("GEMINI_API_KEY")

    @property
    def gemini_model(self) -> str:
        return self.get("GEMINI_MODEL", "gemini-2.5-flash")

    @property
    def fal_key(self) -> str:
        return self.get("FAL_KEY")

    @property
    def fal_default_image_model(self) -> str:
        return self.get("FAL_DEFAULT_IMAGE_MODEL", "fal-ai/flux/schnell")

    @property
    def firecrawl_api_key(self) -> str:
        return self.get("FIRECRAWL_API_KEY")

    @property
    def wonderful_api_key(self) -> str:
        return self.get("WONDERFUL_API_KEY")

    @property
    def wonderful_webhook_url(self) -> str:
        return self.get("WONDERFUL_WEBHOOK_URL")

    @property
    def boxd_api_key(self) -> str:
        return self.get("BOXD_API_KEY")

    @property
    def oumi_api_key(self) -> str:
        return self.get("OUMI_API_KEY")

    @property
    def treg_api_key(self) -> str:
        return self.get("TREG_API_KEY")

    @property
    def hardware_webhook_url(self) -> str:
        return self.get("HARDWARE_WEBHOOK_URL")

    def status(self) -> Dict[str, dict]:
        """Returns connection/configuration status for each hackathon sponsor & tool."""
        return {
            "google_gemini": {
                "name": "Google Gemini",
                "configured": bool(self.gemini_api_key),
                "mode": f"Live ({self.gemini_model})" if self.gemini_api_key else "Simulation Fallback",
                "env_var": "GEMINI_API_KEY",
            },
            "fal": {
                "name": "fal.ai (Content & Digital Art)",
                "configured": bool(self.fal_key),
                "mode": "Live API" if self.fal_key else "Placeholder SVG Preview",
                "env_var": "FAL_KEY",
            },
            "firecrawl": {
                "name": "Firecrawl (Web Research)",
                "configured": bool(self.firecrawl_api_key),
                "mode": "Firecrawl Cloud" if self.firecrawl_api_key else "Direct HTTP Scraper Fallback",
                "env_var": "FIRECRAWL_API_KEY",
            },
            "wonderful": {
                "name": "Wonderful (Voice & Enterprise)",
                "configured": bool(self.wonderful_api_key or self.wonderful_webhook_url),
                "mode": "Live Enterprise Webhook" if (self.wonderful_api_key or self.wonderful_webhook_url) else "Local Action Log",
                "env_var": "WONDERFUL_API_KEY",
            },
            "biotech_apis": {
                "name": "Biotech Open APIs (UniProt / OpenTargets / ChEMBL)",
                "configured": True,
                "mode": "Live Public REST APIs (No Key Required)",
                "env_var": None,
            },
            "boxd": {
                "name": "boxd (Agent Sandbox)",
                "configured": bool(self.boxd_api_key),
                "mode": "boxd Cloud Sandbox" if self.boxd_api_key else "Local Restricted Python Eval",
                "env_var": "BOXD_API_KEY",
            },
            "oumi": {
                "name": "Oumi (Eval & Fine-Tuning)",
                "configured": bool(self.oumi_api_key),
                "mode": "Configured" if self.oumi_api_key else "Local Judge Heuristic",
                "env_var": "OUMI_API_KEY",
            },
            "treg": {
                "name": "treg (Tool Registry)",
                "configured": bool(self.treg_api_key),
                "mode": "Configured" if self.treg_api_key else "Local Tool Registry",
                "env_var": "TREG_API_KEY",
            },
        }


settings = Settings()
