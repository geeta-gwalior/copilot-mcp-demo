from fastapi import FastAPI

app = FastAPI(title="Student Management API")

students = [
    {"id": 1, "name": "Alice Johnson", "age": 20, "grade": "A"},
    {"id": 2, "name": "Bob Smith", "age": 21, "grade": "B"},
    {"id": 3, "name": "Charlie Brown", "age": 19, "grade": "A"},
]


@app.get("/students")
def get_students():
    return students
