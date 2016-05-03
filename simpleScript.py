#!/usr/bin/env python

import, serial, fcntl, os, sys, MySQLdb

fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
print("launching simpleScript, please wait.")

print("setup communication with Arduino and database")
Xbee = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
Xbee.close()
Xbee.open()

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="patate", db="projetSas")
cursor = conn.cursor()

print("ready to launch the loop.")

try:
	while True:
		arduinodata = Xbee.readline().decode("utf-8")
		if arduinodata:
			print("i get : %s", arduinodata)
			arduinotable = arduinodata.split('\t')
			for row in arduinotable:
				cursor.execute("INSERT %s INTO projetSas", arduinotable[])
				pass
			pass
		cursor.execute("SELECT * from projetSas")
		cursor.fetchall()

		Xbee.writelines(raspberrypidata)
		pass
	pass
except KeyboardInterrupt:
	print("let me alive, plaise.")
finally:
	print("Goodbye.")
	pass