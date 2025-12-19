from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/", response_model=schemas.showUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.showUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)