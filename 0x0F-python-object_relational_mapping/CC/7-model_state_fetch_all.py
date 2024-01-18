#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

rows = session.query(State.id, State.name).order_by(State.id)

for row in rows:
    print("{}: {}".format(row[0], row[1]))
