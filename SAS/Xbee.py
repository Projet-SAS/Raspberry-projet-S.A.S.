import serial as serial

class comXbee:
	"""docstring for comXbee"""
	def __init__(self, port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1):
		super(comXbee, self).__init__()
		self.port = port
		self.baudrate = baudrate
		self.timeout = timeout

		serial = serial.Serial()
		serial.port = self.port
		serial.baudrate = self.baudrate
		serial.timeout = self.timeout
		serial.open()

	def requestData(self):
		dataGet = serial.readline().decode("utf-8")
		if dataGet:
			return dataGet
			pass
		else:
			print("Nope.")
			pass
		pass

	def logData(self, logType, logMsg, logBroadcast):
			logPack = "[" + str(logType) + "] " + str(logMsg)
			print(str(logPack))
			if logBroadcast:
				serial.writelines(str(logPack))
				pass
		pass