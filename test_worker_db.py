from fastapi.testclient import TestClient

from app import app
client = TestClient(app)


def test_create_record():
    response = client.post('/v1/create/record', json={"code": 0, "url": "url", "status": 0, "parsing_data": "text"})
    assert response.status_code == 200
    assert response.json() == {"record": "created"}
