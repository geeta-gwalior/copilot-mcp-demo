# Student Management API

A simple FastAPI application that serves a list of sample students from memory.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the app

```bash
uvicorn app:app --reload
```

Then open http://127.0.0.1:8000/students to view the full student list in JSON format.

## Endpoints

### GET /students

Returns all students.

### GET /students/{id}

Returns the student with the matching ID.

Example:

```bash
curl http://127.0.0.1:8000/students/2
```

If no student matches the provided ID, the API returns HTTP 404 with a JSON error:

```json
{ "detail": "Student not found" }
```

### DELETE /students/{id}

Deletes the student with the matching ID and returns the deleted student as JSON.

Example:

```bash
curl -X DELETE http://127.0.0.1:8000/students/2
```

If no student matches the provided ID, the API returns HTTP 404 with a JSON error:

```json
{ "detail": "Student not found" }
```

## Run tests

```bash
pytest
```
