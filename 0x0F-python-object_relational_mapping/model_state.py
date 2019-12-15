#!/usr/bin/python3
"""Start link class to table in database
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                unique=True,
                nullable=False,
                autoincrement="auto",
                primary_key=True)

    name = Column(String(128), nullable=False)
