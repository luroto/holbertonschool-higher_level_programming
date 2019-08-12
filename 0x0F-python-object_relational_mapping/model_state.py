#!/usr/bin/python3
""" This file contains the declaration of a class """
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ This section defines States"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, index=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
