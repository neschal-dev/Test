from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # Used when receiving data from frontend


class UserResponse(UserBase):
    user_id: int  # Used when sending data back to frontend

    model_config = {"from_attributes": True}
