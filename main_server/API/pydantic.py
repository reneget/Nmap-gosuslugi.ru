from pydantic import BaseModel

class UserProperties(BaseModel):
    user_id: int
    key: str