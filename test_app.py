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


def test_delete_student_success():
    # Backup original list and restore after test to avoid affecting other tests
    from app import students

    original = students.copy()

    try:
        response = client.delete("/students/2")
        assert response.status_code == 200
        assert response.json() == {"id": 2, "name": "Bob Smith", "age": 21, "grade": "B"}

        # Ensure student is removed from the list
        get_resp = client.get("/students")
        assert get_resp.status_code == 200
        assert {s["id"] for s in get_resp.json()} == {1, 3}
    finally:
        # Restore original students list
        students.clear()
        students.extend(original)


def test_delete_student_not_found():
    from app import students

    original = students.copy()

    try:
        response = client.delete("/students/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Student not found"}
    finally:
        students.clear()
        students.extend(original)


def test_delete_removes_student_from_list():
    # Ensure that after deleting a student, the student is no longer present in the list
    from app import students

    original = students.copy()

    try:
        # Ensure the student is present before deletion
        assert any(s["id"] == 3 for s in students)

        resp = client.delete("/students/3")
        assert resp.status_code == 200
        assert resp.json()["id"] == 3

        get_resp = client.get("/students")
        assert get_resp.status_code == 200
        assert not any(s["id"] == 3 for s in get_resp.json())
    finally:
        students.clear()
        students.extend(original)
