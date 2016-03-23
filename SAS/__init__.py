# -*- coding: utf-8 -*
#!/usr/bin/env python
import os
import sys
import time
import fcntl
import serial as serial
import .ia as ia
import .ui as ui
import .Xbee as com

serial = serial.Serial()
serial.port = "/dev/ttyUSB0"
serial.baudrate = 9600
serial.timeout = 1
serial.open()

""" processData()

take data & process it
"""
def processData(Input):
	tempRef = 22.0
	lumRef = 600
	print("[process] input : " + str(Input))
	dataIn = Input.split('_')
	global temp
	temp = float(dataIn[0])
	global lum
	lum = float(dataIn[1])
	pass

""" logData()

"""
def logData(logType, logMsg, logBroadcast):
	logPack = "[" + str(logType) + "] " + str(logMsg)
	print(str(logPack))
	if logBroadcast:
		serial.writelines(str(logPack))
		pass
	pass


class launch:
	"""docstring for launch"""
	def __init__(self):
		fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
		net = com.comXbee()
		logData("INFOS", "Projet S.A.S. en cours de lancement", True)
		logData("INFOS", "Lancement de la boucle de recherche de modules de communication..", False)

		try:
			while True:
				logData("INFOS", "Recherche d'informations entrante", False)
				if net.requestData():
					processData(net.requestData())
					logData("INFOS", "J'ai reçu une donnée", False)
					pass
				try:

					pass
				except IOError:
					time.sleep(0.01)
					continue
				pass
			pass
		except KeyboardInterrupt:
			print('\n')
			print("Key Interrupt")
			logData("WARNING", "Key Interrupt - le script est interrompu.", True)
		finally:
			print("Please, reboot.")
			pass