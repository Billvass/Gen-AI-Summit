from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert set(["search", "analyze", "act"]).issubset(set(data["available_tools"]))


def test_run_agent_endpoint():
    payload = {"goal": "Prepare a short demo summary"}
    response = client.post("/api/agent/run", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["goal"] == payload["goal"]
    assert len(data["plan"]) == 3
    assert len(data["steps"]) == 3
    assert payload["goal"] in data["deliverable"]


def test_run_agent_requires_goal():
    response = client.post("/api/agent/run", json={})
    assert response.status_code == 422
