#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('launching sasScript... please wait.')
from sas import * 

net = Xbee.connect("/dev/ttyUSB0", 9600, 1)

try:
    while True:
        print("launch loop.")
        if net.read():
            net.decompose()
        pass
        RaspberryData = database.getrequires()
        net.send(RaspberryData)
    pass
except KeyboardInterrupt:
    print('\n')
    print("Une interruption est survenue")
finally:
    print("OK.")
    pass