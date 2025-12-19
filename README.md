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