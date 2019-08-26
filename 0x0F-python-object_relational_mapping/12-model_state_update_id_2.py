#!/usr/bin/python3
"""
This script updates the name of a State object
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == '__main__':

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    upa = session.query(State).filter(State.id == 2).one()
    upa.name = "New Mexico"
    session.commit()
    session.close()
