#!/usr/bin/python3
"""
This file contains the definition of City class 
"""
from sqlalchemy import Column, Integer, String
from model_state import Base
class City(Base):
    """ This file defines City class""" 
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, index=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    states.id = Column(Integer, nullable=False, foreign_key=True)
