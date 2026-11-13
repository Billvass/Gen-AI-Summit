import base64
import html
from typing import Any, Dict
import httpx
from backend.config import settings


async def generate_media_fal(prompt: str, aspect_ratio: str = "16:9") -> Dict[str, Any]:
    """
    Generates digital art / concept imagery via fal.ai (default model: fal-ai/flux/schnell).
    When FAL_KEY is not configured yet, generates a stylized SVG concept preview data URI.
    """
    fal_key = settings.fal_key
    model = settings.fal_default_image_model

    if fal_key:
        try:
            async with httpx.AsyncClient(timeout=45.0) as client:
                resp = await client.post(
                    f"https://fal.run/{model}",
                    headers={
                        "Authorization": f"Key {fal_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "prompt": prompt,
                        "image_size": "landscape_16_9" if aspect_ratio == "16:9" else "square_hd",
                        "num_inference_steps": 4,
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                images = data.get("images", [])
                image_url = images[0].get("url") if images else None
                if image_url:
                    return {
                        "provider": f"fal.ai ({model})",
                        "status": "generated",
                        "prompt": prompt,
                        "image_url": image_url,
                    }
        except Exception as exc:
            return {
                "provider": "fal.ai (fallback_after_error)",
                "status": "fallback_preview",
                "error_note": str(exc),
                "prompt": prompt,
                "image_url": _build_svg_preview_data_uri(prompt),
            }

    return {
        "provider": "fal_svg_preview (Add FAL_KEY in .env or Settings for live FLUX generation)",
        "status": "preview_ready",
        "prompt": prompt,
        "image_url": _build_svg_preview_data_uri(prompt),
    }


def _build_svg_preview_data_uri(prompt: str) -> str:
    safe_prompt = html.escape(prompt[:95])
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="800" height="450">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0f172a"/>
          <stop offset="50%" stop-color="#1e1b4b"/>
          <stop offset="100%" stop-color="#042f2e"/>
        </linearGradient>
        <radialGradient id="glow" cx="70%" cy="35%" r="45%">
          <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.45"/>
          <stop offset="60%" stop-color="#818cf8" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="800" height="450" fill="url(#bg)"/>
      <rect width="800" height="450" fill="url(#glow)"/>
      <circle cx="560" cy="175" r="110" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 6" opacity="0.7"/>
      <circle cx="560" cy="175" r="70" fill="none" stroke="#a855f7" stroke-width="3" opacity="0.8"/>
      <polygon points="560,115 615,210 505,210" fill="none" stroke="#2dd4bf" stroke-width="2.5" opacity="0.85"/>
      <rect x="48" y="48" width="210" height="32" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
      <text x="66" y="69" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">FAL.AI STUDIO PREVIEW</text>
      <text x="48" y="340" fill="#f8fafc" font-family="sans-serif" font-size="22" font-weight="bold">Generative Visual Concept</text>
      <text x="48" y="372" fill="#94a3b8" font-family="sans-serif" font-size="14">{safe_prompt}...</text>
      <text x="48" y="408" fill="#2dd4bf" font-family="monospace" font-size="12">Add FAL_KEY to switch from SVG synth to live fal-ai/flux/schnell</text>
    </svg>"""
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"
