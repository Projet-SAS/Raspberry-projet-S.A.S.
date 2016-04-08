#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import fcntl
import os
import sys

fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

class connect:
	"""docstring for connect"""
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

	def send(self, data):
		self.arduino.writelines(data)
		print("sended : " + str(data))
		pass

	def decompose(self):
		print("decompose")
		pass