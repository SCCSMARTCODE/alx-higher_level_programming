#!/usr/bin/python3

from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_0_usa", pool_pre_ping=True)

with engine.connect() as connection:
    # Create states table if it doesn't exist
    connection.execute("""
        CREATE TABLE IF NOT EXISTS state1 (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            population INT
        );
    """)

    # Insert data into the states table
    connection.execute("""
        INSERT INTO state1 (name, population)
        VALUES ('California', 39538223),
               ('Texas', 29145505),
               ('Florida', 21538187);
    """)
