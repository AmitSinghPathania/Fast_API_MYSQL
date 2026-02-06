from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    mobile: str
    event_notification: str
    notification_groups: Optional[str] = None
    event_types: str
    is_active: bool = True

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True