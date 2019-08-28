import tkinter as tk
from tkinter import *
import random
from time import sleep
import threading

class clock:
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
		win.title("Window")
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s))
		self.lbl.grid(row = _x , column = _y)
		self.btn = Button(win, text ="configurar reloj", command = popup_clock_config)
		self.btn.grid(row = _x+1, column = _y)
		self.t = threading.Thread(target=self.clk.start , args=(self.lbl, ))
		self.t.start()
def popup_clock_config():
	ven = Toplevel()
	label1 = Label(ven, text = 'Introduce la hora que deseas')
	label1.grid(row=0, column=0)
	entrada=Entry(ven)
	entrada.grid(row=0, column=1)
	b1 = Button(ven, text= "Cambiar hora", command= ven.destroy )
	b1.grid(row=1, column=1)

win = tk.Tk()
win.geometry("230x150")
win.resizable(0,0)
clk1 = GUIClock(win,0,0)
clk2 = GUIClock(win,0,1)
clk3 = GUIClock(win,2,0)
clk4 = GUIClock(win,2,1)
win.mainloop()
