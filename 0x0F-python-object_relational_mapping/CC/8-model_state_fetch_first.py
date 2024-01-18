#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

session = sessionmaker(bind=engine)()

row = session.query(State.id, State.name).first()

if not row:
    print("")
else:
    print(f"{row[0]}: {row[1]}")

