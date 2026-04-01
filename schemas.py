from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    status: str


class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str