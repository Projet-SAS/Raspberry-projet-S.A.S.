# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, sys, time, fcntl, serial
import core, frame, xbeeInit

if __name__ == '__main__':
	temp = 0.0
	lum = 0.0
	fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)

	core.logData("INFOS", "Raspberry est ok.", True)
	core.logData("INFOS", "recherche de modules xbee", False)
	serial.writeline("coucou")
	try:
		while True:
			line = serial.readline().decode("utf-8")
			if line:
				core.processData(line)
				core.logData("INFOS", "temperature : " + str(temp) + ' C', False)
				pass
			try:
				linin = sys.stdin.readline()
				if linin:
					serial.writelines(linin)
					core.logData("OUTPUT", "data send : " + linin, False)
					pass
				pass
			except Exception, e:
				time.sleep(0.01)
				print(e)
			finally:
				linin=False
				pass

	except KeyboardInterrupt:
		print("\n")
		print("Key interrupt")
		core.logData("ERROR", "RPI is disconnected.", True)

	finally:
		print("script down, please reboot.")
