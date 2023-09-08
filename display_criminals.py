# display_criminals.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Criminal

# Create a session to interact with the database
engine = create_engine('sqlite:///criminals.db')
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve all criminals from the database
criminals = session.query(Criminal).all()

# Display the criminal data in a table format
print("Criminals:")
print(f"{'ID':<3}{'Name':<20}{'Crime Committed':<30}{'Date of Arrest':<20}")
print("="*75)
for criminal in criminals:
    print(f"{criminal.id:<3}{criminal.name:<20}{criminal.crime_committed:<30}{criminal.date_of_arrest.strftime('%Y-%m-%d %H:%M:%S'):<20}")

# Close the session
session.close()
