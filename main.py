"""Raspberry Pi project SAS

Partie Raspberry du projet S.A.S. en python.
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial
import core
from xbeeInit import *

if __name__ == '__main__':
	temp = 0.0
	lum = 0.0
	fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

	print "[INFOS] Raspberry est ok."
	serial.writelines("[INFOS] Raspberry est ok.")
	print "recherche de modules xbee"

	try:
		while True:
			line = serial.readline().decode("utf-8")
			if line:
				core.processData(line)
				print("[INFOS] temperature : " + str(temp) + ' C')
				pass
			try:
				linin = sys.stdin.readline()
				if linin:
					serial.writelines(linin)
					print("[output] data send : " + linin)
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
		serial.writelines("RPI is disconnected.")

	finally:
		print("script down, please reboot.")