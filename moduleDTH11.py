#module readHDT11
from guizero import *
import Adafruit_DHT
""" install moduleDTH11
sudo apt update
sudo apt install build-essential python-dev
git clone http://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT"""

class moduleDTH11:
    def __init__(self,app, pin,grid):
        self.grid = grid
        self.temp = 0
        self.humi = 0
        self.app = app
        self.sensor = Adafruit_DHT.DHT11
        self.DHT11_pin = pin
        self.createUI()
    def createUI(self):
        txt = Text(self.app,text = "DTH11\n"+"temp: "+str(self.temp)+"\n"+
                                "humi: "+str(self.humi)+"\n",grid=self.grid,align="left")
    def update(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor,self.DHT11_pin)
        if humidity is not None and temperature is not None:
            self.humi = humidity
            self.temp = temperature
            txt.value =  "DTH11\n"+"temp: "+str(self.temp)+"\n"+"humi: "+str(self.humi)+"\n"
        else:
            info("error", "Failed to get reading from the sensor")
