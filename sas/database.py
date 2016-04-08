#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, mysql.connector

# http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite

# sudo apt-get install python-pip libmysqlclient-dev python-dev python-mysqldb
# pip install mysql
# pip install MySQL-python
# pip install mysql-connector-python --allow-external mysql-connector-python

# conn = mysql.connector.connect(host="localhost", user="root", password="patate", database="projetsas")
# cursor = conn.cursor()
# conn.close()

class db:
	"""docstring for db"""
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

		self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
		self.cursor = self.conn.cursor()

	def cursor(self, query):
		self.cursor.execute(query)
		rows = self.cursor.fetchall()
		pass