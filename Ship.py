import pygame



#This class will contain the size and the status of the ship.

Sunk = 0
Afloat = 1
class Ship:
    def __init__(self):
        self.size=[]
        self.status=""

    def add_size(self, n: int):
        for i in range(n):
            self.size.append(Afloat)

    def change_size(self,n:int):
        for i in range(len(self.size)):
            if (i==n):
                self.size[i]=Sunk

    def change_status(self):
        if 1 not in self.size:
            self.status = "Sunk"
        else:
            self.status = "Afloat"
    
    def __repr__(self):
        return '{} ({})'.format(self.status, self.size)
        

    
        


    

    
