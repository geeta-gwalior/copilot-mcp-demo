from fastapi import FastAPI, HTTPException

app = FastAPI(title="Student Management API")

students = [
    {"id": 1, "name": "Alice Johnson", "age": 20, "grade": "A"},
    {"id": 2, "name": "Bob Smith", "age": 21, "grade": "B"},
    {"id": 3, "name": "Charlie Brown", "age": 19, "grade": "A"},
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """Delete a student by ID. Returns the deleted student on success or 404 if not found."""
    for idx, student in enumerate(students):
        if student["id"] == student_id:
            deleted = students.pop(idx)
            return deleted

    raise HTTPException(status_code=404, detail="Student not found")
