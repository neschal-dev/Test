from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud

# 1. Added the explicit 'prefix=' keyword argument
router = APIRouter(prefix="/users", tags=["Users"])


# 2. Added response_model here so FastAPI knows to filter the output
@router.post("/register", response_model=schemas.UserResponse)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user_object = crud.create_user(db=db, user_data=user_in)

    # FastAPI now looks at response_model=schemas.UserResponse,
    # sees 'from_attributes=True' in your schema, extracts user_id,
    # username, and email, and ignores the password entirely!
    return new_user_object
