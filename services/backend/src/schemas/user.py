from datetime import datetime
from pydantic import BaseModel, constr

class UserBaseSchema(BaseModel):
    username: str
    email: str
    photo: str
    role: str
    created_at: datetime 
    updated_at: datetime

    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: str
    password: constr(min_length=8)

class UserResponseSchema(UserBaseSchema):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class FilteredUserResponse(UserBaseSchema):
    id: str