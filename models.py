
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
	pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String, nullable=False)
    telegramid=Column(Integer, nullable=False)

class Approach:
    id = Column(Integer, primary_key=True, index=True)
    telegramid = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    exercise_id = Column(String, nullable=False)



class Workout(Base, Approach):
    __tablename__ = 'workouts'
    weight = Column(Integer)
    count = Column(Integer, nullable=False)

class Cardio(Base, Approach):
    __tablename__ = 'cardio'
    distance = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)

class Exercises(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    telegramid = Column(Integer, nullable=False)
    weighting = Column(Boolean, nullable=False)
    counting = Column(Boolean, nullable=False)
    timing = Column(Boolean,nullable=False)
    created_at = Column(DateTime, nullable=False)
    exercise_name = Column(String, nullable=False)

