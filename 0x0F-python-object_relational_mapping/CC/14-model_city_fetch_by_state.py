#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def run():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    rows = session.query(State, City).join(City).all()

    for row in rows:
        print("{}: ({}) {}".format(
            row[0].__dict__['name'], row[1].__dict__['id'], row[1].__dict__['name']
            ))


if __name__ == '__main__':
    run()
