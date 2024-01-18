#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

session = sessionmaker(bind=engine)()

add_x = State(name = "Louisiana")

session.add(add_x)
session.commit()

x_id = session.query(State.id).filter(State.name == "Louisiana").scalar()

print(x_id)
