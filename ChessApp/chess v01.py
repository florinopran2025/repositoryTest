

class Table: 

    def __init__(self):
        # column is ["A","B","C","D","E","F","G","H"] (left -> right)
        self.columns=["A","B","C","D","E","F","G","H"]
        # row is [1,2,3,4,5,6,7,8] (down -> top)
        self.rows=[8,7,6,5,4,3,2,1]
    
    def drawTable(self,piece):

        print(" + ",end=" ")
        for i in self.columns:
            print (" "+str(i),end=" ")
        print(" + ")
        for i in range (0,30):
            print("-",end="")
        print()

        # print(" + ",1,2,3,4,5,6,7,8," + ")
        for row in self.rows:
            for column in self.columns:
                if column=="A":
                    print(" "+str(row)+"|", end=" ")
                print(column+str(row), end=" ")
                if column=="H":
                    print("|"+str(row)+" ", end=" ")
            print()
    
        for i in range (0,30):
            print("-",end="")
        print()
        print(" + ",end=" ")
        for i in self.columns:
            print (" "+str(i),end=" ")
        print(" + ")


        

        



class Pieces: # keeps all the pieces
    def __init__(self,color,place):
        """All pieces have a color and a place"""
        self.color=color # black/white
        self.place=place # place (should be a tuplet)


class Pawns(Pieces):    
    def __init__(self,color,place,everMoved):
        super().__init__(color,place)
        self.everMoved=everMoved # True/False
        moveOptions=[(place[0]+1,place[1])]
        if self.everMoved=="False":
            self.moveOptions.append()


table=Table()
table.drawTable(0)





