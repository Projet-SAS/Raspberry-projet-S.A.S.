# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial
import core, frame
from xbeeInit import *

if __name__ == '__main__':
	temp = 0.0
	lum = 0.0
	fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

	logData(INFOS, "Raspberry est ok.", True)
	logData(INFOS, "recherche de modules xbee", False)

	try:
		while True:
			line = serial.readline().decode("utf-8")
			if line:
				core.processData(line)
				logData(INFOS, "temperature : " + str(temp) + ' C', False)
				pass
			try:
				linin = sys.stdin.readline()
				if linin:
					serial.writelines(linin)
					logData(OUTPUT, "data send : " + linin, False)
					pass
				pass
			except Exception, e:
				time.sleep(0.01)
				print(e)
			finally:
				linin=False
				pass

	except KeyboardInterrupt:
		print("\n")
		print("Key interrupt")
		logData(ERROR, "RPI is disconnected.", True)

	finally:
		print("script down, please reboot.")