from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contacts_book import ContactBook
import re
validate_phone_number_pattern = "^[0-9]{10,11}$"

app = FastAPI()
book = ContactBook()

class Contact(BaseModel):
    name: str
    phone: str

@app.post("/contacts")
def add_contact(contact: Contact):
     if not re.match(validate_phone_number_pattern, contact.phone):
        raise HTTPException (status_code = 400, detail= "Invalid phone number!")
     book.add(contact.name,contact.phone)
     return {"message": "Added successfully!"}

@app.get("/contacts")
def list_contacts():
    return book.list_all()
     

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    book.delete(name)
    return {"message": "Removed successfully!"}

@app.get("/contacts/{name}")
def find_contact(name: str):
    result = book.find(name)
    if not result:
     raise HTTPException(status_code=404, detail="Contact not found!")
    return book.find(name)



