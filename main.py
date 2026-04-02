from contacts_book import ContactBook
import re #import to find match regex
validate_phone_number_pattern = "^[0-9]{10,11}$" #pattern to validate
validate_for_name_pattern = "^[A-Za-z0-9_-]+$"
book = ContactBook()
book.loadContacts()
while True:
    action = input("Command (add/delete/find/list/save/quit): ")
    
    if action == "add":
     while True:
        name = input("Name: ")        
        if not re.match(validate_for_name_pattern, name) :
            print("Invalid input")
            continue # go back to ask for name (to the start of loop)
        else :
            break
     while True:    
         phone = input("Phone: ")      
         if not re.match(validate_phone_number_pattern, phone):
            print("Invalid phone number!")
            continue
         else:
            break
 
     book.add(name, phone)    
          
    elif action == "find" :
        name = input("Name you want to find? :")
        book.find(name)
        
    elif action == "delete" :
        name = input("Name you want to delete? :")
        book.delete(name)
        
    elif action == "list" :
        book.list_all()
    
    elif action == "save" :
        book.saveContacts()
            
    elif action == "quit":
        break
    else :
        print("Invalid command")