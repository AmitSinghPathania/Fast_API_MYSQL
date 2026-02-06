from sqlalchemy.orm import Session
from . import models, schemas

def get_contacts(db: Session):
    return db.query(models.EmergencyContact).all()

def get_contact_by_id(db: Session, contact_id: int):
    # print("contact_id",contact_id)
    return db.query(models.EmergencyContact).filter(models.EmergencyContact.mobile == contact_id).first()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.EmergencyContact(**contact.dict())
    print("insert",db_contact)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: int, contact: schemas.ContactCreate):
    db_query = db.query(models.EmergencyContact).filter(models.EmergencyContact.id == contact_id)
    contact_obj = db_query.first()
    if contact_obj:
        db_query.update(contact.dict())
        db.commit()
        return contact_obj
    return None

def delete_contact(db: Session, contact_id: int):
    db_query = db.query(models.EmergencyContact).filter(models.EmergencyContact.id == contact_id)
    contact_obj = db_query.first()
    if contact_obj:
        db_query.delete()
        db.commit()
        return True
    return False