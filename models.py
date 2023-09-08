# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a SQLite database named 'criminals.db'
engine = create_engine('sqlite:///criminals.db')

# Create a base class for declarative models
Base = declarative_base()

# Define the Criminal table
class Criminal(Base):
    __tablename__ = 'criminals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    crime_committed = Column(String, nullable=False)
    date_of_arrest = Column(DateTime, default=datetime.now)

# Create the table in the database
Base.metadata.create_all(engine)
