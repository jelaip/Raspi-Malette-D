from guizero import Box, PushButton
from buttonClass import *

class matriceBt:
    def __init__(self,app,grid,ligne,colone,waffle):
        self.grid = grid
        self.ligne = ligne
        self.colone = colone
        self.app = app
        self.matrix = waffle
        self.createMat()
    def createMat(self):
        box = Box(self.app,layout="grid", grid=self.grid)
        for x in range(self.ligne):
            for y in range(self.colone):
                b = buttonClass(box,self.matrix,x,y,self.ligne,self.colone)
