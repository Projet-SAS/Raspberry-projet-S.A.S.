# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import time
import fcntl
import serial as serial
import SAS

serial = serial.Serial()
serial.port = "/dev/ttyUSB0"
serial.baudrate = 9600
serial.timeout = 1
serial.open()

temp = 0.0
lum = 0.0

fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
SAS.logData("INFOS", "Raspberry en marche.", True)
SAS.logData("INFOS", "Recherche de modules Xbee", False)

if __name__ == '__main__':
	try:
		while True:
			SAS.logData("INFOS", "Recherche d'informations IN", False)
			lineIn = serial.readline().decode("utf-8")
			if lineIn:
				SAS.processData(lineIn)
				SAS.logData("INFOS", "Temperature : " + str(temp) + 'C', False)
				pass
			try:
				SAS.logData("INFOS", "Recherche d'informations OUT", False)
				lineOut = sys.stdin.readline()
				if lineOut:
					serial.writelines(lineOut)
					SAS.logData("SEND", "Data : ", + lineOut, False)
					pass
				pass
			except Exception, e:
				time.sleep(0.01)
				print(e)
			finally:
				lineOut = False
				pass
			pass
		pass
	except KeyboardInterrupt:
		print("\n")
		print("Key Interrupt")
		SAS.logData("WARNING", "Le Raspberry est deconnecte", False)
	finally:
		print("Script have been stop, please reboot.")
		pass
