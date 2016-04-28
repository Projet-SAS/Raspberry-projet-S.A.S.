#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring for setup

setup du projet S.A.S. Récupère les données envoyées par l'arduino via des radios fréquences,
il enregistre le tout sur une database puis lit les besoins de l'utilisateur pour l'envoyer à l'arduino.
"""

from sas import *
print('launching sasScript... please wait.')

net = Xbee.Connect("/dev/ttyUSB0", 9600, 1)

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
