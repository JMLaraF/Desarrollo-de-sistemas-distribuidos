import socket
import time
from tkinter import *
import tkinter as tk
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def RunClient(lbl, port):       #Crea un hilo que recibe info del servidor y la proyecta
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        while(1):
            time.sleep(0.001)
            s.sendall(b'Hello, world')
            data = s.recv(4)
            lbl.config(text = "%02d" % int(repr(data)[2:-1]))
        s.shutdown(socket.SHUT_RDWR)
        s.close()


type = int(input()) # Recibe un numero desde consola, 0 Para recibir horas , 1 para recibir minutos, 2 para recibir segundos.
win = tk.Tk()
win.geometry("100x50")
lbl = Label(win , text="%02d" % (0))
lbl.grid(row = 0 , column = 0 , columnspan = 2)
clientThread = threading.Thread(target = RunClient , args = (lbl, PORT+type, ))
clientThread.setDaemon(True)
clientThread.start()
win.mainloop()
