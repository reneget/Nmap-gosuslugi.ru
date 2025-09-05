from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    full_name: str
    position: str
    secret_key: str
    counter: int

class User_update(BaseModel):
    full_name: Optional[str] = None
    position: Optional[str] = None

class User_create(BaseModel):
    full_name: str
    position: str
    secret_key: str
