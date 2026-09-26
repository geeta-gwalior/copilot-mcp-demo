from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_students_returns_sample_data():
    response = client.get("/students")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Alice Johnson", "age": 20, "grade": "A"},
        {"id": 2, "name": "Bob Smith", "age": 21, "grade": "B"},
        {"id": 3, "name": "Charlie Brown", "age": 19, "grade": "A"},
    ]
