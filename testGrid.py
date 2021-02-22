from guizero import *
from matriceBt import *
from menuBar import *
from moduleLed import *
from time import sleep
#from moduleDTH11 import *
#tabPositionnement

app = App(title="Systeme D", width=350, height=350, layout="grid")
menu = MenuBarItem(app)
"""behaviourLedSlider = Combo(app,options=["off","blink","on"],grid=[1,0],align="left")
behaviourLedTxt = Text(app,text = "led 1 ",grid=[0,0],align="left")
readHDT11Txt = Text(app,text = "led 2 ",grid=[0,1],align="left")
readHDT11Box = CheckBox(app, grid=[1,1], align="left")
typeOfUnityTxt = Text(app,text = "unite ",grid=[0,2],align="left")
typeOfUnity = ButtonGroup(app,options= [["d°","D"],["f°","f"]],
    selected="M",horizontal=True, grid=[1,2], align="left")
def GetValue():
    info("Booking", "Thank you for booking")
    print( behaviourLedSlider.value )
    print( readHDT11Box.value )
    print( typeOfUnity.value )
def do_nothing():
    return 0
def AllumeLed(matrice,x,y):
    if matrice[x,y].color == "red":
        matrice[x,y].color="white"
    else:
        matrice[x,y].color = "red"
btGetValue = PushButton(app, command=GetValue, text="GetValue", grid=[2,0], align="left")"""
#DHT = moduleDTH11(pin =4,app=app,grid=[1,0])
waffle = Waffle(app, grid=[0,1], height= 3 , width=3)
matrice = matriceBt(app=app,grid=[0,2],ligne=3,colone=3,waffle=waffle)
led = moduleLed(app=app,grid=[0,0],textLed="switch led", colorLed= "blue",pin= 1)
#matrice.createMat()
#DHT.update();
i=0;
while True:
    sleep(2)
    i= i+1
    print(i)
    app.display()
