import os, sys, time, fcntl, serial
serial = serial.Serial()
serial.port = "/dev/ttyUSB0"
serial.baudrate = 9600
serial.timeout = 1
serial.open()
