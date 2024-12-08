import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import User, Workout, Cardio, Exercises
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)

Session = sessionmaker(engine)
#with Session() as session:

