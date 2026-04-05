import os, mysql.connector
class ContactBook:
  def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="contacts_db"
        )
  
 
        pass  # pass if file not existed
  
  def add (self,name, phone): 
    cursor = self.db.cursor()
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) # "%s"prevent from SQL Injection
       result = cursor.fetchone()  # fetch one row only
       if result:
         print("This name has been added!")
       else:
            cursor.execute("INSERT INTO contacts VALUES (%s, %s)", (name, phone))
            self.db.commit()
            print ("Successfully add this contact !")
    finally:
        cursor.close() #close cursor to prevent memory leaks
   
  def delete (self,name):
    cursor = self.db.cursor()
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) # "%s"prevent from SQL Injection
       result = cursor.fetchone()  
       if not result:
         print("Invalid contacts!")
       else:
            cursor.execute("DELETE FROM contacts WHERE name = %s", (name,)) # DELETE doesn't use INTO or VALUES — just WHERE to specify which one to delete."    
            self.db.commit()
            print ("Successfully delete this contact !")
    finally:
        cursor.close() 
        
      
  def find(self, name):
    cursor = self.db.cursor()
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) 
       result = cursor.fetchone()  
       if not result:
         print("Invalid contacts!")
       else:
             return(f"Found: {result[0]} - {result[1]}")
    finally:
        cursor.close() 
    
  def list_all(self):
   cursor = self.db.cursor()
   try:
       cursor.execute("SELECT * FROM contacts")
       result = cursor.fetchall()   #fetch all rows
       if not result:
         return("None contacts available!")
       else:
             for index, (name, phone) in enumerate(result): 
              return(f"{index + 1} : {name} - {phone}")
   finally:
        cursor.close() 
  
      


