import run
import pytest

@pytest.fixture
def client():
    app = run.app.test_client()
    return app

def test_get(client):
    res = client.get('/api/random')
    assert res.status_code == 200

def test_grenzen(client):
    res = client.get('/api/random')
    assert res.json("randomNumber") > 1 and res.json("randomNumber") < 100