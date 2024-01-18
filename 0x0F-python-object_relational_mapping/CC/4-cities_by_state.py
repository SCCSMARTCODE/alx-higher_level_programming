#!/usr/bin/python3

import MySQLdb
import sys

dbname = sys.argv[3]

connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

cc = connect.cursor()

cc.execute("""
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
GROUP BY cities.id
ORDER BY cities.id;
        """)

ccans = cc.fetchall()

for row in ccans:
    print(row)

cc.close()
connect.close()
