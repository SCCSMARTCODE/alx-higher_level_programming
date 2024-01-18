#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

session = sessionmaker(bind=engine)()

change = session.query(State).filter(State.name.like("%a%")).all()

if change:

    for del_ in change:
        session.delete(del_)

    session.commit()
