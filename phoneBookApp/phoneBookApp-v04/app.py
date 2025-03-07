import os
from contacts import *


app=StartApp()


while app.gameon:    
    app.menu.displayMenu()
    opt=int(input("What do you want?"))
    if opt==1: # display contacts
        app.contacts.optDisplayContacts()        
    elif opt==2: # search contact
        app.contacts.optSearchContact()
    elif opt==3: # sort contacts
        app.contacts.optSortContacts()
    elif opt==4: # add contact
        app.contacts.addContact()
    elif opt==5: # save contacts
        app.contacts.optSaveContacts()
    elif opt==6: # load contacts
        app.contacts.optLoadContacts()
    elif opt==7: # switch language
        app.menu.optSwitchLanguage()  
    elif opt==8: # app version
        app.version() 
    elif opt==0: # exit
        app.gameon=False    
    else: # unrecognised option
        app.contacts.unknownOption()
    app.continueGame()
    
