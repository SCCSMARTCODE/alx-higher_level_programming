#!/usr/bin/python3

import MySQLdb
import sys

dbname = sys.argv[3]

connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

cc = connect.cursor()

cc.execute("""
SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4], ))

ccans = cc.fetchall()

tmp = list(row[0] for row in ccans)
print(*tmp, sep=", ")

cc.close()
connect.close()
