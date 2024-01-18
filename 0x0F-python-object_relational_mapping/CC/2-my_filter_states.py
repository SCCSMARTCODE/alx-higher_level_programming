#!/usr/bin/python3

import MySQLdb
import sys

pydb = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
pyc = pydb.cursor()
pyc.execute(f"SELECT * FROM states WHERE name = '{sys.argv[4]}';")
result = pyc.fetchall()
for row in result:
    print(row)

pyc.close()
pydb.close()
