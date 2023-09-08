# add_criminal.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Criminal

# Create a session to interact with the database
engine = create_engine('sqlite:///criminals.db')
Session = sessionmaker(bind=engine)
session = Session()

# Get user input for criminal data
name = input("Enter criminal's name: ")
crime = input("Enter the crime committed: ")

# Create a new Criminal instance
new_criminal = Criminal(name=name, crime_committed=crime)

# Add the new criminal to the database
session.add(new_criminal)
session.commit()

print("Criminal added successfully!")

# Close the session
session.close()

