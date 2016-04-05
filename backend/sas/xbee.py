#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, fcntl
import os, sys

fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

class net():
	"""docstring for net"""
	def __init__(self, port, baudrate, timeout):
		self.port = port
		self.baudrate = baudrate
		self.timeout = timeout

		self.arduino = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
		self.arduino.close()
		self.arduino.open()
		self.arduino.writelines("connection is open")

	def read(self):
		print("search data : wait.")
		arduinoData = self.arduino.readline().decode("utf-8")
		if arduinoData:
			print(arduinoData)
			pass
		pass

	def send(self):
		raspberryData = sys.stdin.readline()
		if raspberryData:
			self.arduino.writelines(raspberryData)
			print("sended : " + str(raspberryData))
			pass
		pass