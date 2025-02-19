from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/v1/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is healthy ✅"}

def test_sentiment_analysis():
    response = client.post("/v1/analyze/", json={"text": "I love this!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()