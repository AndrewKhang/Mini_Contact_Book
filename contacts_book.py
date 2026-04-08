import os, mysql.connector
class ContactBook:
  def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # Default for XAMPP
            database="contacts_db"
        )
  
 
        pass  # pass if file not existed
  
  def add (self,name, phone): 
    cursor = self.db.cursor(dictionary=True)
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) # "%s"prevent from SQL Injection
       result = cursor.fetchone()  # fetch one row only
       if result:
            return{"message" : "This name has been added!"}
       cursor.execute("INSERT INTO contacts VALUES (%s, %s)", (name, phone))
       self.db.commit()
       return {"message": "Successfully add this contact !"}
    except Exception as e :
      print(f"[ERROR] add() failed: {str(e)}") # Log error for debugging
      raise # Re-raise to let FastAPI handle the error response
    finally:
        cursor.close() #close cursor to prevent memory leaks
   
  def delete (self,name):
    cursor = self.db.cursor(dictionary=True)
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) # "%s"prevent from SQL Injection
       result = cursor.fetchone()  
       if not result:
         return{"message":"Invalid contacts!"}
       cursor.execute("DELETE FROM contacts WHERE name = %s", (name,)) # DELETE doesn't use INTO or VALUES — just WHERE to specify which one to delete."    
       self.db.commit()
       return {"message":"Successfully delete this contact !"}
    except Exception as e : 
      print(f"[ERROR] delete() failed: {str(e)}") # Log error for debugging
      raise # Re-raise to let FastAPI handle the error response
    finally:
        cursor.close() 
        
  def update(self, name, phone) :
    cursor = self.db.cursor(dictionary=True)
    try: 
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,))
       result = cursor.fetchone()
       if not result:
         return{"message":"Invalid contacts!"}
       else: 
            cursor.execute("UPDATE contacts SET phone = %s WHERE name = %s",(phone, name))     
            self.db.commit()
            return {"message":"Successfully update this contact !"}
    except Exception as e:
     print(f"[ERROR] update() failed: {str(e)}")
     raise
    finally:
        cursor.close() 
        
  def find(self, name):
    cursor = self.db.cursor(dictionary=True)
    try:
       cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,)) 
       result = cursor.fetchone()  
       if not result:
         return{"message":"Invalid contacts!"}
       else:
             return result
    except Exception as e:
     print(f"[ERROR] find() failed: {str(e)}")
     raise
    finally:
        cursor.close() 
    
  def list_all(self):
   cursor = self.db.cursor(dictionary=True)
   try:
       cursor.execute("SELECT * FROM contacts")
       result = cursor.fetchall()   #fetch all rows
       return result
   except Exception as e:
            # Log error for debugging (in production, you should use proper logging)
            print(f"[ERROR] list_all() failed: {str(e)}")
            raise
   finally:
        cursor.close() 
  
      


