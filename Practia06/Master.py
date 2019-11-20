import socket
import mysql.connector
from time import sleep
import threading

class Master:
	def __init__():
		self.listOfServers = ["-1"]*256
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		self.IP = s.getsockname()[0]
		self.PORT = 60428
		s.close()
		self.isCordinator = False
		self.cordinador = Cordinador(self.listOfServers,self.IP)
		self.sincronizador = Sincronizador()


	def Run(self):
		isOneEnable = self.cordinador.mapListOfServers()
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		sock.bind(self.IP , self.PORT)
		sock.settimeout(1.0)
		if(isOneEnable == "-1")
			self.cordinador.cordinadorIP = self.IP
		else:
			sock.sendto(b'GMC' ,(isOneEnable,self.cordinador.PORT))
			data , addr = sock.recvfrom(100)
			self.cordinador.cordinadorIP = data.decode('utf-8').split()

		while not self.isCordinator:
			if(self.cordinador.cordinadorIP == self.IP)
				self.isCordinator = True
				break
			
			try:
				sock.sendto(b'AYE',(self.cordinador.cordinadorIP,self.cordinador.PORT))
				data , addr = sock.recvfrom(100)
				msg = data.decode('utf-8').split()
				if(msg[0] == "YBR")
					continue
			except socket.Timeouterror as ex:
				self.cordinador.Eleccion()
	
		self.sincronizador.start(self.listOfServers,self.IP)


		

class Cordinador:
	def __init__(self, listOfServers,IP):
		self.listOfServers = listOfServers
		self.IP = IP
		self.PORT = 60430
		self.cordinadorIP = "-1"
		cordListenThread = threading.Thread(target=self.cordinadorListener)
		cordListenThread.setDaemon(True)
		cordListenThread.start()
#	def findEnableServers():
#		print("Declare subNet")
#		IPx = input()
#		for i in range(2,250):

	def Eleccion(self):
		dominios = self.IP.split('.')
		AuxIp = dominios[0] + '.' + dominios[1] + '.' + dominios[2] + '.'
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		sock.settimeout(0.5)
		isOneEnable = False
		for i in range(int(dominios[3]),254):
			try:
				sock.sendto(b'AYE',(AuxIp + str(i) , self.PORT))
				data , addr = sock.recvfrom(100)
				msg = data.decode('utf-8').split()
				if(msg[0] == "YBR")
					isOneEnable = True
					break;
			except socket.Timeouterror as ex:
		mapListOfServers()
		if(not isOneEnable):
			self.cordinadorIP = self.IP
			for i in range(2,254):
				if(self.listOfServers[i] != "-1"):
					sock.sendto(b'SEC',(self.listOfServers[i] , self.PORT))
		sock.close()
		while(self.cordinadorIP == "-1"):
			sleep(1.0)			


	def mapListOfServers(self)
		dominios = self.IP.split('.')
		AuxIp = dominios[0] + '.' + dominios[1] + '.' + dominios[2] + '.'
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		sock.settimeout(0.5)
		someOneEnable = "-1"
		for i in range(2,254):
			try:
				sock.sendto(b'AYE',(AuxIp + str(i) , self.PORT))
				data , addr = sock.recvfrom(100)
				msg = data.decode('utf-8').split()
				if(msg[0] == "YBR")
					self.listOfServers[i] = AuxIp + str(i)
					someOneEnable = AuxIp + str(i)
			except socket.Timeouterror as ex:
				self.listOfServers[i] = "-1"
		sock.close()
		return someOneEnable

	def cordinadorListener(self):
		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        sock.bind((self.IP , self.PORT))
		while True:
            data , addr = sock.recvfrom(100)
            cmdArgs = data.decode('utf-8').split()
            print(cmdArgs[0])
            if(cmdArgs[0] == "AYE"):
				sock.sendto(b'YBR',(addr))
			elif(cmdArgs[0] == "MLLE"):
				self.cordinadorIP = "-1"
				sock.sendto(b'YBR',(addr))
			elif(cmdArgs[0] == "SEC"):
				self.cordinadorIP = addr[0]
			elif(cmdArgs[0] == "GMC"):
				sock.sendto(self.cordinadorIP.encode('utf-8'),(addr))
	


class Sincronizador:
	
	def __init__(self):
		self.PORT = 60432
		self.mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="Tiempo"
		)
		self.mycursor = self.mydb.cursor()

	def toTime(self,num):
		cadena = ""
		cadena += str(num//10000)+":"
		num -= (num//10000)*10000
		cadena += str(num//100)+":"
		num -= (num//100)*100
		cadena += str(num)
		return cadena

	def makeAjust(self,sock , listOfServers):
		prom = 0 
		if(len(listOfServers) > 0):
			for x in listOfServers:
				if(x != "-1"):
					print("[%s , %d]" % (x , self.PORT) )
					sock.sendto(b'GTM',(x,self.PORT))
					data , addr = sock.recvfrom(100)
					prom += int(data.decode('utf-8'))
					print(prom)
			prom = prom // len(listOfServers)
			MSG = "CTM " + str(prom)
			hora = self.toTime(prom)
			sqlformula = "INSERT INTO Tiempo (hora) VALUES(\"%s\")"
			self.mycursor.execute(sqlformula,(hora,))
			self.mydb.commit()
			for x in listOfServers:
				if(x != "-1"):
					sock.sendto(MSG.encode('utf-8'),(x,self.PORT))
			

	def start(self,listOfServers,IP):


		sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		sock.bind((IP,self.PORT-1))
	#	sock.settimeout(0.5)

		while True:
			try:
				print("Consulta")
				self.makeAjust(sock,listOfServers)
				sleep(2.0)
			except KeyboardInterrupt as k:
				break
