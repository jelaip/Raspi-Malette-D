from guizero import *
from matriceBt import *
from menuBar import *
from moduleLed import *
from time import sleep
from moduleDTH11 import *

app = App(title="Systeme D", width=350, height=350, layout="grid")
menu = MenuBarItem(app)
affle = Waffle(app, grid=[0,1], height= 3 , width=3)
matrice = matriceBt(app=app,grid=[0,2],ligne=3,colone=3,waffle=waffle)
led = moduleLed(app=app,grid=[0,0],textLed="switch led", colorLed= "red",pin= 25)
DHT = moduleDTH11(pin =4,app=app,grid=[1,0])
#matrice.createMat()
DHT.update();
app.display()
