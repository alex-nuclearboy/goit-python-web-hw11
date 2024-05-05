from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone_number: str = Field(max_length=15)
    birthday: date
    additional_info: Optional[str] = None


class ContactModel(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
