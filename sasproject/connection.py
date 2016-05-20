#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring for connection

"""
import serial
import MySQLdb


class Arduino(object):
    """Connect to arduino with Xbee"""
    def __init__(self, ubsport, baudrate, timeout):
        """init xbee connection
        close before open to be sure there is no other open connection.
        """
        self.Xbee = serial.Serial(ubsport, int(baudrate), timeout=int(timeout))
        self.Xbee.close()
        self.Xbee.open()

    def read(self):
        """Read input data with rf
        only read, for advanced process use the right class.

        """
        print("[raspberry] sending request")
        arduino_input = self.Xbee.readline().decode("utf-8")
        return arduino_input

    def write(self, data_in):
        """write output data with rf
        be sure to check your syntax.
        """
        self.Xbee.writelines(data_in)
        pass

    def __del__(self):
        """Close connection on interrupt"""
        self.Xbee.close()


class Database(object):
    """Class to access to the database"""
    def __init__(self, host, user, password, dbname):
        """init mysql database connection
        require host, user, password, dbname
        """
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
