from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate):
    # 1. Fake hash the password
    hashed_password = user_data.password + "hashed_pass_12#11"

    # 2. Dump the Pydantic data into a dict, but EXCLUDE the plain-text password
    user_dict = user_data.model_dump(exclude={"password"})

    # 3. Create the SQLAlchemy object using the remaining valid fields
    db_user = User(**user_dict)
    
    # 4. Attach the hashed password using dot notation
    db_user.hashed_password = hashed_password

    # 5. Save to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user