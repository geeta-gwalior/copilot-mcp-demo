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


def test_get_student_returns_matching_student():
    response = client.get("/students/2")

    assert response.status_code == 200
    assert response.json() == {"id": 2, "name": "Bob Smith", "age": 21, "grade": "B"}


def test_get_student_returns_404_when_not_found():
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
