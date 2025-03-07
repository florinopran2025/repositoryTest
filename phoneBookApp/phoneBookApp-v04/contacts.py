import os

# -------------- GENERAL TOOLS -----------------

# DIRECTORY
filePath=os.path.abspath(__file__)
fileDirectory =os.path.dirname(filePath)+"\\"


# MENU DICTIONARY (based on file)
fileMenu=open(fileDirectory+"file.menu","r")
englishDict={}
romanianDict={}
for row in fileMenu:
    if row.startswith("englishDict") or row.startswith("romanianDict"):
        row=row.strip()
        (language,no,opt)=row.split("=",maxsplit=2)
        if language=="englishDict":
            englishDict[int(no)]=opt 
        else:
            romanianDict[int(no)]=opt   
fileMenu.close()
MENU ={        # construct dictionary MENU (extracted from file)
    "english": englishDict,
    "romanian": romanianDict
}


class StartApp():
    def __init__(self):        
        self.gameon=True
        self.menu=Menu("english")
        self.contacts=Contacts()
    def continueGame(self):
        input("Press ENTER to continue...")
    # APP VERSION
    def version(self):
        file=open(fileDirectory+"readme.txt","r")
        for line in file:
            print(line)
        file.close()
    # WRONG COMMAND
    def unknownOption(self):
        print ("Nu such option in the menu.😒")
    

class Menu:
    def __init__(self,language):
        self.language=language
    def displayMenu(self):
        os.system('cls')
        print("--- --- MENU --- ---")
        for key, value in MENU[self.language].items():
            print (f"{key} - {value}")
        print()
    # 7 = SWITCH LANGUAGE
    def optSwitchLanguage(self):
        if self.language=="english":
            self.language= "romanian"
        else:
            self.language= "english"
    


class NewContact:
    def __init__(self,contactName, contactPhone, contactEmail):
        self.name=contactName
        self.phone=contactPhone
        self.email=contactEmail

class Contacts:
    def __init__(self):
        self.contacts=[]        
        self.opt=0
        

    def __str__(self):
        return self.names

    # ----------------------------------------------------
    # ---------------- GENERAL METHODS -------------------
    # USED BY THE MAIN METHODS 
    def switchContacts(self, i,j):
        #contacts.names
        aux=self.contacts[i].name
        self.contacts[i].name=self.contacts[j].name
        self.contacts[j].name=aux
        #phones
        aux=self.contacts[i].phone
        self.contacts[i].phone=self.contacts[j].phone
        self.contacts[j].phone=aux
        #emails
        aux=self.contacts[i].email
        self.contacts[i].email=self.contacts[j].email
        self.contacts[j].email=aux   

    def searchByContactName(self,nameSearched):
        self.optLoadContacts() 
        foundIt=False
        for i in range (0,len(self.contacts)):
            if nameSearched.lower()==self.contacts[i].name.lower():
                print(f"{self.contacts[i].name} has the number: {self.contacts[i].phone}")
                foundIt=True
        if foundIt==False:
            print(f"You dont' have {nameSearched}\'s number.")

    # ----------------------------------------------------
    # --------------------- ACTIONS FROM MENU ------------
    # 1 = DISPLAY CONTACTS
    def optDisplayContacts(self):           
        print("Total number of contacts:",len(self.contacts))
        for i in range (0,len(self.contacts)):
            print (f"{i+1}.  {self.contacts[i].name}\'s phone is {self.contacts[i].phone}. \n"
                   f"You can reach him/her at {self.contacts[i].email}.")
        
    # 2 = SEARCH CONTACT (BY NAME)
    def optSearchContact(self):
        nameSearched=input("Name of contact?")
        self.searchByContactName(nameSearched)

    # 3 = SORT CONTACTS
    def optSortContacts(self):
        self.optLoadContacts()    
        length=len(self.contacts)
        for i in range (0,length-1):
            for j in range (i+1,length):
                if self.contacts[i].name>self.contacts[j].name:
                    self.switchContacts(i,j)
        self.optSaveContacts()
        print ("The list was successfully sorted. Here it is:")
        self.optDisplayContacts()

    # 4 = ADD CONTACT
    def addContact(self):        
        contactName=input("Name:")
        contactPhone=input("Phone:")
        contactEmail=input("Email:")
        self.contacts.append(NewContact(contactName,contactPhone,contactEmail))
        print(f"You've successfully added {contactName} in your phone book.")

    # 5 = SAVE CONTACTS
    def optSaveContacts(self):
        file=open(fileDirectory+"phoneBookDataBase.csv",'w')
        for i in range (0,len(self.contacts)):        
            file.write(f"{self.contacts[i].name},{self.contacts[i].phone},{self.contacts[i].email}")
            file.write("\n")
        print(f"{len(self.contacts)} have been saved in cloud.")
        file.close()

    # 6 = LOAD CONTACTS
    def optLoadContacts(self):    
        self.contacts=[]
        file=open(fileDirectory+"phoneBookDataBase.csv",'r')
        numberOfContacts=0
        for line in file:
            numberOfContacts+=1
            line=line.strip()
            nameOnEachLine,phoneOnEachLine,emailOnEachLine=line.split(",")
            self.contacts.append(NewContact(nameOnEachLine,phoneOnEachLine,emailOnEachLine))
        print ("You've successfully loaded",numberOfContacts,"contacts.")    
        file.close()



    



