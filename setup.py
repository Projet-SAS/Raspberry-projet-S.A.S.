#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring for setup

setup du projet S.A.S. Récupère les données envoyées par l'arduino via des radios fréquences,
il enregistre le tout sur une database puis lit les besoins de l'utilisateur pour l'envoyer à l'arduino.
"""
import sys
import sasproject


pythonVersion = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
print("python version: %s" % pythonVersion)

config = {
    "name": "projet-S.A.S.",
    "version": "alpha-3.0",
    "author": "keikyoku",
    "author_email": "benjamin.boboul@gmail.com",
    "repo_url": "https://github.com/Projet-SAS/Raspberry-projet-S.A.S.",

    "dbuser": "root",
    "dbpass": "patate",
    "dbhost": "127.0.0.1",
    "dbname": "projetSas",

    "xbee_port": "/dev/ttyUSB0",
    "xbee_baudrate": 9600,
    "xbee_timeout": 1
}

sasproject.setup(**config)
