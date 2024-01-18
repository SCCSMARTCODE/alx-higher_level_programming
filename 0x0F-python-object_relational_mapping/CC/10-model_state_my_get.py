#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

session = sessionmaker(bind=engine)()

pass_ = argv[4]
pass_ = pass_.split(" ")[0]

row = session.query(State.id).filter(State.name == pass_).first()

if not row:
    print("No found")
else:
    print(f"{row[0]}")

