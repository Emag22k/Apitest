from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]

class CreatedUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

class UpdatedUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime
