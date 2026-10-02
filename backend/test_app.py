
from app import app


def test_home_returns_success():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Backend is working!"


def test_health_returns_healthy():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "healthy"
