#!/usr/bin/python3
""" This script lists the first object from some database"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter_by(id=1).order_by(
                State.id.asc()):
        print("{}: {}".format(instance.id, instance.name))
    session.close()
