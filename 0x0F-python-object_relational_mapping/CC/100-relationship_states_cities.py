#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sys import argv as a
from relationship_state import Base, State
from relationship_city.py import City

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(a[1], a[2], a[3]))


session = sessionmaker(bind=engine)()

add_x = City(name="San Francisco")
add_y = State(name="California")
add_y.cities

session.add()
