# Pornim un nou program care are clasa Menu si clasa MenuItem
 
# Create 5 menuItem objects luand label-ul din fisierul en.menu
 
# deci clasa MenuItem are constutctor, str si membri id si label 
# programul se numeste menuLoader.py
 
# in fisierul en.menu avem:
# - menuItem1=Read 
# - menuItem2=Print
# - menuItem3=Search 
# - menuItem4=Save 
# - menuItem5=Exit

# deci folosim if, while, functii, citireDinFisier, clase

import os

thePath=os.path.abspath(__file__)
theDir =os.path.dirname(thePath)+"\\"

class MenuItem:
    def __init__(self,id):
        file=open(theDir+"en.menu","r")
        # self.mLabel=[]
        self.mItem=[]
        for line in file:
            (firstPart,secondPart)=line.strip().split("=")
            # self.mLabel.append(firstPart)
            self.mItem.append(secondPart)
            
        file.close()
        # self.displayedLabel=self.mLabel[id]
        self.displayedItem=self.mItem[id]

    def __str__(self):
        return self.displayedItem

class Menu:
    def __init__(self):
        self.option=[]
        for id in range (0,5):
            self.option.append(MenuItem(id))
        
    def printMenu(self,id):
        print (self.option[id])

menu=Menu()

os.system('cls')

print("--------------------------")
print("----- O P T I O N S ------")
print("--------------------------")

menu.printMenu(0)
menu.printMenu(1)
menu.printMenu(2)
menu.printMenu(3)
menu.printMenu(4)