
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    # TODO: Распипсать поля 

class Workout(Base):
    __tablename__ = 'workouts'

    # TODO: Распипсать поля 
