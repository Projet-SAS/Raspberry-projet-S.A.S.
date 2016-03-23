# -*- coding: utf-8 -*
#!/usr/bin/env python
import serial as serial
import .ia
import .ui
import .Xbee

serial = serial.Serial()
serial.port = "/dev/ttyUSB0"
serial.baudrate = 9600
serial.timeout = 1
serial.open()

"""processData

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

def logData(logType, logMsg, logBroadcast):
	logPack = "[" + str(logType) + "] " + str(logMsg)
	print(str(logPack))
	if logBroadcast:
		serial.writelines(str(logPack))
		pass
	pass