#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, mysql.connector


# http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite

# sudo apt-get install python-pip libmysqlclient-dev python-dev python-mysqldb
# pip install mysql
# pip install MySQL-python
# pip install mysql-connector-python --allow-external mysql-connector-python

conn = mysql.connector.connect(host="localhost", user="root", password="patate", database="projetsas")
cursor = conn.cursor()
conn.close()