
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_homepage():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to DeployDeck!",
        "status": "running"
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
