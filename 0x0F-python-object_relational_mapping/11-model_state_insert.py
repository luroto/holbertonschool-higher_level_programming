#!/usr/bin/python3
""" This script lists all State objects from some database
    which contains some letter
"""
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
    luis = State(name='Louisiana')
    session.add(luis)
    session.commit()
    print(luis.id)
    session.close()
