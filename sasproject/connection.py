#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring for connection

"""
import serial
import MySQLdb


class Arduino(object):
    """Connect to arduino with Xbee"""
    def __init__(self, ubsport, baudrate, timeout):
        """"""
        print("xbee class")
        self.Xbee = serial.Serial(ubsport, baudrate, timeout=timeout)
        self.Xbee.close()
        self.Xbee.open()

    def read(self):
        """"""
        print("[raspberry] sending request")
        arduino_input = self.Xbee.readline().decode("utf-8")
        return arduino_input

    def __del__(self):
        """"""
        self.Xbee.close()


class Database(object):
    """Class to access to the database"""
    def __init__(self, host, user, password, dbname):
        """"""
        self.conn = MySQLdb.connect(host=host, user=user, passwd=password, db=dbname)
        self.cursor = self.conn.cursor()

        pass

    def cursor(self, query):
        """"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
        pass

    def __del__(self):
        """"""
        self.conn.close()
