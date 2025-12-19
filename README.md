# FastAPI Backend
A backend API built with FastAPI, focused on clean architecture, secure configuration, and production ready deployment

This repository is intentionally minimal and structured to reflect real world backend practices

## Tech Stack
- Python
- FastAPI
- JWT Authentication
- SQLAlchemy
- Uvicorn

## Project Structure
```
fastapi-backend
├── blog
│   └── repository
|   |   ├── blog.py             # Helper functions for blog routers
|   |   ├── user.py             # Helper functions for user routers
|   └── routers
│   │   ├── __init__.py
│   │   ├── authentication.py
|   |   ├── blog.py
│   │   └── user.py
|   ├── _init__.py
|   ├── database.py
|   ├── JWTtoken.py
|   ├── main.py.py              # Application entry point
|   ├── models.py
|   ├── oauth2.py
|   ├── schemas.py
├── .gitignore
├── blog.db                     # Database
├── main.py
├── README.md
├── requirements.txt
```

## Setup (Local)
```
git clone https://github.com/m-sipho/fastapi-backend.git
cd fastapi-backend
python -m venv .venv
.venv\Scripts\Activate.ps1      # For Windows powershells
pip install -r requirements.txt
uvicorn blog.main:app --reload
```
API available at:
- `/docs` - API documentation
