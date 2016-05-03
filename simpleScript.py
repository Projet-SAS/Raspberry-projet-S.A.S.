#!/usr/bin/env python

import serial, fcntl, os, sys, MySQLdb

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
			print("i get : %s" % arduinodata)
			arduinotable = arduinodata.split('\t')
			
			datatable = {"temperature": {"zone1": arduinotable[0], "zone2": arduinotable[2], "outside": arduinotable[3]}, "luminosity": {"zone1sensor1": datatable[4], "zone1sensor2": datatable[5], "zone2sensor1":datatable[6], "zone2sensor2":datatable[7]}, "movement": []}

			cursor.execute("INSERT INTO luminosity(luminosityonezoneone, luminositytwozoneone, luminosityonezonetwo, luminositytwozonetwo) VALUES(`%f`, `%f`, `%f`, `%f`), " % datatable["luminosity"]["zone1sensor1"], datatable["luminosity"]["zone1sensor2"], datatable["luminosity"]["zone2sensor1"], datatable["luminosity"]["zone2sensor2"])
			pass
		raspberrypidata = cursor.execute("SELECT * from requirements ORDER BY idrequirements DESC LIMIT 1")
		# raspberrypidata = cursor.fetchall()

		Xbee.writelines(raspberrypidata)
		pass
	pass
except KeyboardInterrupt:
	print("let me alive, plaise.")
finally:
	print("Goodbye.")
	pass
