import tkinter as tk
from tkinter import *
from datetime import datetime
import random
from time import sleep
import threading
now = datetime.now() # Fecha y hora actuales

class clock:	#Clase Reloj
	"""def __init__(self, hours, minutes, seconds, secTimer):#inicializamos el reloj con estos valores
		self.h = hours	#Horas
		self.m = minutes
		self.s = seconds
		self.status = True#El reloj avanza o no
		self.secTimer = 1 #Valor del sleep para los segundos"""
	def __init__(self):
		self.h = int(now.strftime("%H"))
		self.m = int(now.strftime("%M"))
		self.s = int(now.strftime("%S"))
		self.secTimer = 1 #Valor del sleep para los segundos
		self.status = True
	def start(self , lbl):	#El thred de cada GUIClock llamara a esta funcion
		while(1): #While true para que siempre cheque el status y actualice el reloj
			#print(self.status)
			if(self.status==True):	#Status del reloj, sirve para pausarlo
				sleep(self.secTimer)	#Segun el valor del atributo secTimer es la pausa
				self.s += 1
				if(self.s >= 60 ): #Reset de los segundos si se pasa de 60
					self.s = 0
					self.m += 1
				if(self.m >= 60): #Reset de los minutos si se pasa de 60
					self.m = 0
					self.h += 1
				if(self.h >= 24):#Reset de las horas si se pasa de 24
					self.h = 0
				lbl.config(text = "%02d:%02d:%02d" % (self.h , self.m , self.s))
			else:
				sleep(1)
	def pauseClock(self):
		self.status=False
	def resumeClock(self):
		self.status=True

class randclock(clock): #Clase heredada para relojes con valores aleatorios
	def __init__(self): #Sobrecargamos el constructor para que el reloj empiece con valores aleatorios
		self.h = random.randint(0,23)
		self.m = random.randint(0,59)
		self.s = random.randint(0,59)
		self.status = True
		self.secTimer = 1

class GUIClock:		#La GUI del reloj estara definida en esta clase
	def __init__(self, win, _x , _y): #win es la ventana en la cual colocaremos el reloj, _x y _y es la posicionamiento tipo grid
		self.clk = clock() #Creamos un atributo del tipo clock
		#win.title("Window")
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s)) #Creamos un atributo de clase del tipo label con los valores del reloj
		self.lbl.grid(row = _x , column = _y, columnspan=2)
		self.btnSet = Button(win, text ="configurar reloj", command = lambda: GUIClock.popup_clock_config(self,win)  )#Creamos 2 atributos del tipo Button para la configuracion de los relojes
		self.btnSet.grid(row = _x+1, column = _y)
		self.btnSeg = Button(win, text ="configurar segundero", command = lambda: GUIClock.popup_seg_config(self,win)  )
		self.btnSeg.grid(row = _x+1, column = _y+1)
		self.t = threading.Thread(target=self.clk.start , args=(self.lbl, )) #Creamos un atributo de tipo Thread el cual manejara el avance y actualizacion del reloj
		self.t.start()
	def setTimeGUI(self,win,horas, minutos, segundos): #Funcion que establece los valore del reloj
		print("Horas",horas)
		self.clk.h = int(horas)
		self.clk.m = int(minutos)
		self.clk.s = int(segundos)
		self.clk.status=True
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s))
	def popup_clock_config(self,win):#Funcion para la modificacion de los valores del reloj con GUI
		self.clk.status=False	#Paramos el reloj
		#ven = Toplevel()	#Creamos un ventana pop up
		ven = Toplevel()
		label1 = Label(ven, text = 'Modificar reloj') #Colocamos labels y entries en la ventana pop up
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
		b1 = Button(ven, text= "Cambiar reloj", command= lambda: GUIClock.setTimeGUI(self,win,entradaHoras.get(),entradaminutos.get(),entradaSegs.get() ) or ven.destroy()  )
												#De la clase GUIClock llama a setTimeGUI con estos parametros y destruye la ventana emergente
		b1.grid(row=4, column=0)
		#ven.protocol("WM_DELETE_WINDOW", lambda: resumeClockGUI(self,ven))  Intento de hacer que al cerrar el popu continue el reloj
	"""def resumeClockGUI(self):
		self.clk.status=True
		ven.destroy()"""
	def popup_seg_config(self,win):#Funcion para la modificacion de los valores del reloj con GUI
		self.clk.status=False	#Paramos el reloj
		#ven = Toplevel()	#Creamos un ventana pop up
		ven1 = Toplevel()
		label1 = Label(ven1, text = 'Modificar segundero') #Colocamos labels y entries en la ventana pop up
		label1.grid(row=0, column=0, columnspan=2)
		labelSegundero = Label(ven1, text = 'Introduce cada cuanto se actualizara el segundero del reloj')
		labelSegundero.grid(row=1, column=0)
		entradaSegundero=Entry(ven1)
		entradaSegundero.grid(row=1, column=1)
		bSegs = Button(ven1, text= "Cambiar reloj", command= lambda: GUIClock.setSegGUI(self , entradaSegundero.get() ) or ven1.destroy()  )
												#De la clase GUIClock llama a setTimeGUI con estos parametros y destruye la ventana emergente
		bSegs.grid(row=2, column=0)
	def setSegGUI(self, seg):
		self.clk.secTimer = float(seg)
		self.clk.status = True
class GUIClockRand(GUIClock): #Clase hija de GUIClock, la unica diferencia es que este inicializa un reloj aleatorio
	def __init__(self, win, _x , _y):
		self.clk = randclock()
		#win.title("Window")
		self.lbl = Label(win, text="%02d:%02d:%02d" % (self.clk.h , self.clk.m , self.clk.s))
		self.lbl.grid(row = _x , column = _y, columnspan=2)
		self.btn = Button(win, text ="configurar reloj", command = lambda: GUIClock.popup_clock_config(self,win)  )
		self.btn.grid(row = _x+1, column = _y)
		self.btn = Button(win, text ="configurar segundero", command =lambda: GUIClock.popup_seg_config(self,win)  )
		self.btn.grid(row = _x+1, column = _y+1)
		self.t = threading.Thread(target=self.clk.start , args=(self.lbl, ))
		self.t.start()


win = tk.Tk()

win.geometry("530x200") #Tamaño de la aplicación
win.resizable(1,1)	#Esto permite a la app adaptarse al tamaño
clk1 = GUIClock(win,0,0)	#iniciamos el reloj con valores actuales en la posicion 0, 0
clk2 = GUIClockRand(win,0,3) #Relojes aleatorios
clk3 = GUIClockRand(win,3,0) #Como los botones ocupan dos columnas
clk4 = GUIClockRand(win,3,3)
"""def AlCierredeVentanaPrincipal(): Intento hacer que los hilos se detengan y salgande manera adecuada al cerrar la ventana, para evitar los errores del final
	for i in range(0,3):

	win.destroy()
win.protocol("WM_DELETE_WINDOW",AlCierredeVentanaPrincipal)"""
win.mainloop()
