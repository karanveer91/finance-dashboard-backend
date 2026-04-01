from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    status = Column(String)


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(String)
    notes = Column(String)