import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_api_hello(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert b"message" in response.data
