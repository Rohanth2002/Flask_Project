from test_app import app
import _json
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_tweet_success(client):
    data = {'text': 'Hello, Twitter!'}
    response = client.post('/tweets', json=data)
    assert response.status_code == 201

def test_create_tweet_incomplete_request(client):
   data = {'invalid_key': 'Hello, Twitter!'}
   response = client.post('/tweets', json=data)
   assert response.status_code == 400