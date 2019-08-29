import tkinter as tk
from tkinter import *
from datetime import datetime
import random
from time import sleep
import threading
now = datetime.now() # current date and time

class clock:
	def __init__(self, hours, minutes, seconds):
		self.h = hours
		self.m = minutes
		self.s = seconds
	def __init__(self):
		self.h = int(now.strftime("%H"))
		self.m = int(now.strftime("%M"))
		self.s = int(now.strftime("%S"))

	def start(self , lbl):
		while(1):
			sleep(1)
			self.s += 1
			if(self.s == 60):
				self.s = 0
				self.m += 1
			if(self.m == 60):
				self.m = 0
				self.h += 1
			if(self.h == 24):
				self.h = 0
			lbl.config(text = "%02d:%02d:%02d" % (self.h , self.m , self.s))
		#	print("%02d : %02d : %02d" %(self.h , self.m , self.s))

class randclock(clock):
	def __init__(self, hours, minutes, seconds):
		self.h = hours
		self.m = minutes
		self.s = seconds
	def __init__(self):
		self.h = random.randint(0,23)
		self.m = random.randint(0,59)
		self.s = random.randint(0,59)

	def start(self , lbl):
		while(1):
			sleep(1)
			self.s += 1
			if(self.s == 60):
				self.s = 0
				self.m += 1
			if(self.m == 60):
				self.m = 0
				self.h += 1
			if(self.h == 24):
				self.h = 0
			lbl.config(text = "%02d:%02d:%02d" % (self.h , self.m , self.s))
		#	print("%02d : %02d : %02d" %(self.h , self.m , self.s))

class GUIClock:
	def __init__(self, win, _x , _y):
		self.clk = clock()
		#win.title("Window")
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s))
		self.lbl.grid(row = _x , column = _y, columnspan=2)
		self.btn = Button(win, text ="configurar reloj", command = lambda: popup_clock_config(self))
		self.btn.grid(row = _x+1, column = _y)
		self.btn = Button(win, text ="configurar segundero", command = popup_clock_config)
		self.btn.grid(row = _x+1, column = _y+1)
		self.t = threading.Thread(target=self.clk.start , args=(self.lbl, ))
		self.t.start()
	def setTimeGUI(self,horas, minutos, segundos):
		self.clk.h = int(horas)
		self.clk.m = int(minutos)
		self.clk.s = int(segundos)

class GUIClockRand(GUIClock):
	def __init__(self, win, _x , _y):
		self.clk = randclock()
		#win.title("Window")
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s))
		self.lbl.grid(row = _x , column = _y, columnspan=2)
		self.btn = Button(win, text ="configurar reloj", command = lambda: popup_clock_config(self))
		self.btn.grid(row = _x+1, column = _y)
		self.btn = Button(win, text ="configurar segundero", command = popup_clock_config)
		self.btn.grid(row = _x+1, column = _y+1)
		self.t = threading.Thread(target=self.clk.start , args=(self.lbl, ))
		self.t.start()
def popup_clock_config(Clock):
	ven = Toplevel()
	label1 = Label(ven, text = 'Modificar reloj')
	label1.grid(row=0, column=0, columnspan=2)
	labelHoras = Label(ven, text = 'Introduce las horas')
	labelHoras.grid(row=1, column=0)
	entradaHoras=Entry(ven)
	entradaHoras.grid(row=1, column=1)
	labelminutos = Label(ven, text = 'Introduce los minutos que deseas')
	labelminutos.grid(row=2, column=0)
	entradaminutos=Entry(ven)
	entradaminutos.grid(row=2, column=1)
	labelSeg = Label(ven, text = 'Introduce los segundos que deseas')
	labelSeg.grid(row=3, column=0)
	entradaSegs=Entry(ven)
	entradaSegs.grid(row=3, column=1)
	b1 = Button(ven, text= "Cambiar reloj", command= lambda: GUIClock.setTimeGUI(Clock,entradaHoras.get(),entradaminutos.get(),entradaSegs.get() )  )
	b1.grid(row=4, column=0)

win = tk.Tk()
win.geometry("530x500")
win.resizable(1,1)
clk1 = GUIClock(win,0,0)
clk2 = GUIClockRand(win,0,3)
clk3 = GUIClockRand(win,2,0)
clk4 = GUIClockRand(win,2,3)
win.mainloop()
