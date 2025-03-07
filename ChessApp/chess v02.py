

class Table: 
    # this is the change i want to see in github
    #after that, i will revert it using git reset

    def __init__(self):
        # column is ["A","B","C","D","E","F","G","H"] (left -> right)
        self.columns=["A","B","C","D","E","F","G","H"]
        # row is [1,2,3,4,5,6,7,8] (down -> top)
        self.rows=[8,7,6,5,4,3,2,1]

        # empty matrix (default value assign for each square)
        self.matrix={}
        for row in self.rows:
            for column in self.columns: 
                self.matrix[column+str(row)]="⬜" 

                # self.matrix[column+str(row)]=column+str(row) 


    def drawTable(self,piece):

        # header line
        print(" + ",end=" ")
        for i in self.columns:
            print (""+str(i),end=" ")
        print(" + ")
        for i in range (0,20):
            print("-",end="")
        print()

        # print(" + ",1,2,3,4,5,6,7,8," + ")
        for row in self.rows:
            for column in self.columns:
                if column=="A":
                    print(" "+str(row)+"|", end="")

                # print(column+str(row), end=" ")
                print(piece,end="")

                if column=="H":
                    print("|"+str(row)+" ", end=" ")
            print()
    
        # bottom line
        for i in range (0,20):
            print("-",end="")
        print()
        print(" + ",end=" ")
        for i in self.columns:
            print (""+str(i),end=" ")
        print(" + ")



class Pieces: # keeps all the pieces
    def __init__(self,color,place):
        """All pieces have a color and a place"""
        self.color=color # black/white
        self.place=place # eg. A3


class Pawns(Pieces):    
    def __init__(self,color,place,everMoved):
        super().__init__(color,place)
        self.everMoved=everMoved # True/False
        if color=="black":
            self.symbol="👨🏿‍⚖️"
        else:
            self.symbol="👨🏻‍⚖️"


table=Table()
table.drawTable("⬜")
print(table.matrix)





