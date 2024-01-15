#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

"""City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """

class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)