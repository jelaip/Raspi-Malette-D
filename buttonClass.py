from guizero import PushButton

class buttonClass:
    def __init__(self,box,waffle,x,y,ligne,colone):
        self.x = x
        self.y = y
        self.matrix = waffle
        self.ligne = ligne
        self.colone = colone
        self.box = box
        PushButton(self.box,command=lambda:self.allumeLed(),
                text=(self.x+self.y*self.ligne+1), grid=[self.x,self.y], height=1 , width=2)
    def allumeLed(self):
        if self.x>=self.colone or self.y>=self.ligne:
            return
        if self.matrix[self.x,self.y].color == "red":
            self.matrix[self.x,self.y].color="white"
        else:
            self.matrix[self.x,self.y].color = "red"
