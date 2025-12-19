from typing import List, Annotated
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Session = Depends(database.get_db), ):
    return blog.get_all(db)

# Store blog to database
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)

# Get a blog with a particular id from database
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def read_block_with_id(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], id: int, db: Session = Depends(database.get_db)):
    return blog.read_blog_with_id(id, db)


# Delete a blog with a specific id from the database
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], id: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)

# Update a blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)