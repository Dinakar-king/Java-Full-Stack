
from sqlalchemy import Column, Integer, String, Text
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    skill = Column(String(255), nullable=True)
    resume = Column(Text, nullable=True)  # To store parsed resume data
    certificate = Column(String(255), nullable=True)