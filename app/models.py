from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import Base

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True)
    mobile = Column(String(20))
    event_notification = Column(String(50)) 
    notification_groups = Column(String(255), nullable=True) 
    event_types = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())