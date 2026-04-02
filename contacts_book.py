import os
class ContactBook:
  def __init__(self):
    self.contacts = {}
  
  def loadContacts(self):
    try:
        with open("./ContactBook/contacts.txt", "r") as f:
            for line in f:
                # tách line ra ở đây
                parts = line.split(" - ")
                name = parts[0].split(" : ")[1]
                phone = parts[1].strip()  # strip() xóa \n ở cuối dòng
                self.contacts[name] = phone
    except:
        pass  # file chưa có thì bỏ qua
  
  def add (self,name, phone): 
      # add in self.contacts
      if name in self.contacts :
          print ("This name has been added !")
      else:
       self.contacts[name] = phone
       print ("Successfully add this contact !")

   
  def delete (self,name):
        if name in self.contacts :
          del self.contacts[name]
          print ("Successfully delete this contact!")
        else : 
          print("Invalid contacts")
      
  def find(self, name):
    # find in self.contacts
     if name in self.contacts :
         return (f"Found : {name} - {self.contacts[name]}") 
     else : 
         return("Invalid contacts")
  def list_all(self):
    # print all
    if not self.contacts:
        return("No contacts yet !")
    else:
        for index, (name, phone) in enumerate(self.contacts.items()) :
         return(f"{index + 1} : {name} - {phone}") 
  
  def saveContacts(self):
    #   f = open("./Python/contacts.txt", "x") #create new file
     try: 
      os.makedirs("./ContactBook", exist_ok=True)
      with open("./ContactBook/contacts.txt", "w") as f: #open file
           for index, (name, phone) in enumerate(self.contacts.items()) :
            f.write(f"{index + 1} : {name} - {phone} \n") #write in file
     except Exception as e:
       print(f"Something went wrong: {e}")       


