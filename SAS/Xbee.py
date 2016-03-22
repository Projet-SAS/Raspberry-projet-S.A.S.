import serial as serial

serial = serial.Serial()
serial.port = "/dev/ttyUSB0"
serial.baudrate = 9600
serial.timeout = 1
serial.open()

def scanNet():
	lineIn = serial.readline().decode("utf-8")
	if lineIn:
		SAS.procressData(lineIn)
	pass