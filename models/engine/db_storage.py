#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        '''Used to instantiate engine and create attributes'''
        self.__engine = ('mysql+mysqldb://{}:{}@{}/{}'.format
                         (getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                          getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                         pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None)
