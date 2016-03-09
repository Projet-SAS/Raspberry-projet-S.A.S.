# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial
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
	print(logPack)
	if logBroadcast:
		serial.writeline(logPack)
		pass
	pass