from guizero import Text,CheckBox, Box,PushButton,Waffle
#import RPi.GPIO as GPIO
#from time import sleep

# $ sudo apt-get install python-rpi.gpio python3-rpi.gpio

class moduleLed:
    def __init__(self, app,grid, textLed, colorLed,pin):
        self.app = app
        self.textLed = textLed
        self.colorLed = colorLed
        self.grid = grid
        self.pin = pin
        """GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)"""
        self.createBox()
    def createBox(self):
        box = Box(self.app,layout="grid",grid= self.grid)
        title = Text(box,text="Led pin" + str(self.pin), grid = [0,0],align="left")
        txt = Text(box,text=self.textLed, grid = [0,1],align="left")
        waffle = Waffle(box,grid = [0,2],height =1,width = 1,align = "left")
        waffle[0,0].color = "black"
        btSwitchLed = PushButton(box,grid = [0,1], align = "right",text= "off",
                                pady=1,padx=1,command=lambda:self.switchLed(btSwitchLed.text,btSwitchLed,objwaffle = waffle))
    def switchLed(self, ledValue,obj,objwaffle):
        if(ledValue == "on" or ledValue ==True or ledValue ==1):
            print("off")
            obj.text="off"
            objwaffle[0,0].color = "black"
            #GPIO.output(self.pin, GPIO.LOW)
        if(ledValue == "off" or ledValue ==False or ledValue ==0):
            print("on")
            obj.text="on"
            objwaffle[0,0].color = self.colorLed
            #GPIO.output(self.pin, GPIO.HIGH)
