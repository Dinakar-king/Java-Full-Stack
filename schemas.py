
from pydantic import BaseModel
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    name: str
    skill: Optional[str] = None
    # Resume will store the extracted text from the uploaded file
    resume: Optional[str] = None 
    certificate: Optional[str] = None

# Properties to receive via API on creation
class UserCreate(UserBase):
    pass

# Properties to return to client
class User(UserBase):
    id: int

    class Config:
        #orm_mode = True # Changed from from_attributes = True for Pydantic v1 compatibility if needed, else use from_attributes
        # If using Pydantic v2, from_attributes = True is preferred.
        # For broader compatibility, orm_mode = True is safer if Pydantic version is unknown.
        # Assuming Pydantic v1 for now based on common FastAPI project setups unless specified.
        # If Pydantic v2 is confirmed, this should be: from_attributes = True
        from_attributes = True

# Properties for job suggestion response
class JobSuggestion(BaseModel):
    suggested_title: str
    user_id: int
