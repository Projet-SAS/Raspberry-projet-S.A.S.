#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from . import report, xbee

def core():
	print("core starting")
	net = xbee.net("/dev/ttyUSB0", 9600, 1) #setup the xbee class
	try:
		while True:
			if net.read(): # read informations from the arduino
				net.decompose()
				pass
			try:
				if net.send(): #send data
					print("it's ok")
					pass
			except IOError:
				time.sleep(0.1)
				pass
			pass
		pass
	except KeyboardInterrupt:
		print('\n')
		print("the script have been interrupted.")
	finally:
		pass
	pass
