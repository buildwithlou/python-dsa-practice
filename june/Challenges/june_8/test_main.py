from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# First test, get empty tasks list
def test_get_tasks():
    response = client.get("/tasks?token=secret123")
    assert response.status_code == 200
    assert response.json() == {"tasks": []}


# Second test, create a task
def test_create_task():
    response = client.post(
        "/tasks?token=secret123",
        json={
            "id": 1,
            "title": "Learn FastAPI",
            "status": "todo",
            "description": "Testing!",
        },
    )
    assert response.status_code == 201
    assert response.json()["task"]["title"] == "Learn FastAPI"


# Third test, invalid token
def test_invalid_token():
    response = client.get("/tasks?token=wrongtoken")
    assert response.status_code == 401


# Fourth test, invalid status
def test_invalid_status():
    response = client.post(
        "/tasks?token-secret123",
        json={"id": 2, "title": "Test Task", "status": "invalid"},
    )
    assert response.status_code == 422


# Fifth test, task not found
def test_task_not_found():
    response = client.get("/tasks/999?token=secret123")
    assert response.status_code == 404
