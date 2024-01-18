#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

session = sessionmaker(bind=engine)()

rows = session.query(State.id, State.name).filter(State.name.like("%a%")).order_by(State.id).all()

if not rows:
    print("")
else:
    for row in rows:
        print(f"{row[0]}: {row[1]}")

