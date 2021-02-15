from guizero import *


app = App(title="My second GUI app", width=700, height=500, layout="grid")
behaviourLedSlider = Combo(app,options=["off","blink","on"],grid=[1,0],align="left")
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
btGetValue = PushButton(app, command=GetValue, text="GetValue", grid=[1,3], align="left")
app.display()
