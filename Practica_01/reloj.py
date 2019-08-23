import time
from datetime import datetime
import random 
import math
now = datetime.now() # current date and time

class reloj():
    def __init__(self):
        self.activo = True
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def random_time(self):
        self.hours = math.floor(random.uniform(0,23))
        self.minutes = math.floor(random.uniform(0, 59))
        self.seconds = math.floor(random.uniform(0,59))

    def local_time(self):
        self.hours = int(now.strftime("%H"))
        self.minutes = int(now.strftime("%M"))
        self.seconds = int(now.strftime("%S"))

    def reset_time(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    def change_s(self,s):
        self.seconds= s

    def change_m(self,m):
        self.minutes= m
        
    def change_h(self,h):
        self.hours= h

    def change_status(self):
        if (self.activo):
            self.activo = False
        else:
            self.activo = True

    def show_status(self):
        if (self.activo):
            print(str(self.hours).zfill(2) + ":" +str(self.minutes).zfill(2)+ ":" +str(self.seconds).zfill(2))
        else:
            print("El reloj esta desactivado")




