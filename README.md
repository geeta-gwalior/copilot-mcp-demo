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

Then open http://127.0.0.1:8000/students to view the student data in JSON format.

## Run tests

```bash
pytest
```
