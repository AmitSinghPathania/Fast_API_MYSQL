import uvicorn
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app import models, schemas, database, databasequery 
from typing import List
app = FastAPI()

# app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items", response_model=List[schemas.ContactResponse])
def read_items(db: Session = Depends(database.get_db)):
    return databasequery.get_contacts(db)

@app.get("/items/{item_id}", response_model=schemas.ContactResponse)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    print("item_id",item_id)
    db_contact = databasequery.get_contact_by_id(db, contact_id=item_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.post("/items", response_model=schemas.ContactResponse)
def create_item(contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    return databasequery.create_contact(db=db, contact=contact)

@app.put("/items/{item_id}", response_model=schemas.ContactResponse)
def update_item(item_id: int, contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    updated_contact = databasequery.update_contact(db, item_id, contact)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact
# delele data
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    success = databasequery.delete_contact(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Deleted successfully"}

if __name__ == "__main__":
    # Ensure uvicorn points to the correct app location
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)