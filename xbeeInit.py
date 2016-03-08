	serial = serialSerial()
	serial.port = "/dev/ttyUSB0"
	serial.baudrate = 9600
	serial.timeout = 1
	serial.open()