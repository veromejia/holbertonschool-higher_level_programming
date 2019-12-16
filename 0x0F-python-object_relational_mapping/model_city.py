#!/usr/bin/python3


"""contains the state class"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer,
                unique=True,
                nullable=False,
                autoincrement="auto",
                primary_key=True)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'), nullable=False)
