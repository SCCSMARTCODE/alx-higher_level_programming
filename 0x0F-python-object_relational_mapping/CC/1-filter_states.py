#!/usr/bin/python3

import MySQLdb
import sys

pydb = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
pyc = pydb.cursor()
pyc.execute("SELECT * FROM states WHERE name LIKE 'N%';")
result = pyc.fetchall()
for row in result:
    print(row)

pyc.close()
pydb.close()
