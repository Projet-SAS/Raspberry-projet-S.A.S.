# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import time
import fcntl
import serial as serial
import SAS

temp = 0.0
lum = 0.0

fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
core.logData("INFOS", "Raspberry en marche.", True)
core.logData("INFOS", "Recherche de modules Xbee", False)

if __name__ == '__main__':
	try:
		while True:
			line = serial.readline().decode("utf-8")
			if lineIn:
				core.processData(lineIn)
				core.logData("INFOS", "Temperature : " + str(temp) + 'C', False)
				pass

			try:
				lineOut = sys.stdin.readline()
				if lineOut:
					serial.writelines(lineOut)
					core.logData("SEND", "Data : ", + lineOut, False)
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
		core.logData("WARNING", "Le Raspberry est deconnecte")
	finally:
		print("Script have been stop, please reboot.")
		pass
