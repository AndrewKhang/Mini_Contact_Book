# Mini Contact Book API

A simple contact book REST API built with FastAPI and MySQL.

## Tech Stack
- Python
- FastAPI
- MySQL (XAMPP)
- Pydantic

## How to run
1. Start XAMPP (Apache + MySQL)
2. Activate virtual environment:
```bash
source venv/Scripts/activate
```
3. Run the server:
```bash
uvicorn api:app --reload
```
4. Open `http://127.0.0.1:8000/docs`

## Endpoints
- `GET /contacts` → list all contacts
- `GET /contacts/{name}` → find contact by name
- `POST /contacts` → add new contact
- `DELETE /contacts/{name}` → delete contact

## Validation
- Phone: 10-11 digits only
- Name: letters, numbers, underscore, hyphen only