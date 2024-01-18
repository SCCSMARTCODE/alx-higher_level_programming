#!/usr/bin/python3

from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_0_usa", pool_pre_ping=True)

with engine.connect() as connection:
    # Create states table if it doesn't exist
    result = connection.execute("SELECT * FROM state1")

    rows = result.fetchall()

    for row in rows:
        print(row)
