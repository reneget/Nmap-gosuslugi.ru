import datetime

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    full_name: str
    position: str
    secret_key: str
    is_active: bool
    kill_time: datetime.datetime

class User_update(BaseModel):
    full_name: Optional[str] = None
    position: Optional[str] = None
    is_active: Optional[bool] = None

class User_create(BaseModel):
    full_name: str
    position: str
    secret_key: str
    kill_time: Optional[datetime.datetime] = None
