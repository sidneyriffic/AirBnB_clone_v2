#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        name = ""

    @property
    def cities(self):
        '''
        Get a list of cities based on state.id
        '''
        my_list = []

        for value in models.storage.all(City).values():
            if city.state_id == self.id:
                my_list.append(value)
            return my_list
