import json
from http import HTTPStatus


def test_ping(test_app):
    response = test_app.test_client().get("/ping")
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data.decode())
    assert data == {"message": "Pong!", "status": "success"}
