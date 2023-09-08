# delete_criminal.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Criminal

# Create a session to interact with the database
engine = create_engine('sqlite:///criminals.db')
Session = sessionmaker(bind=engine)
session = Session()

# Display current criminals for reference
criminals = session.query(Criminal).all()
print("Current Criminals:")
print(f"{'ID':<3}{'Name':<20}{'Crime Committed':<30}{'Date of Arrest':<20}")
print("="*75)
for criminal in criminals:
    print(f"{criminal.id:<3}{criminal.name:<20}{criminal.crime_committed:<30}{criminal.date_of_arrest.strftime('%Y-%m-%d %H:%M:%S'):<20}")

# Get user input for the ID of the criminal to delete
criminal_id = input("Enter the ID of the criminal to delete: ")
if criminal_id.isdigit():
    criminal_id = int(criminal_id)
    criminal_to_delete = session.query(Criminal).filter_by(id=criminal_id).first()

    if criminal_to_delete:
        session.delete(criminal_to_delete)
        session.commit()
        print(f"Criminal with ID {criminal_id} deleted successfully.")
    else:
        print(f"No criminal found with ID {criminal_id}.")
else:
    print("Invalid input. Please enter a valid ID.")

# Close the session
session.close()
