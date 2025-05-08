from app import app


def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200


def test_hello():
    tester = app.test_client()
    response = tester.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello from Flask!'}
