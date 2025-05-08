import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the home page returns 200"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask App Deployed" in response.data  # Verify content


def test_api_hello(client):
    """Test API endpoint returns 200 and correct data"""
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello from Flask!"}
