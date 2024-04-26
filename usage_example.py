# Example usage of the InMemoryDB class
from inmemorydb import InMemoryDB

# Create a new database instance
db = InMemoryDB()

# Start a transaction and add some data
db.begin_transaction()
db.put('userID', 1002)    # Username associated with an integer ID
db.put('userScore', 88)   # User's score as an integer
db.commit()

# Retrieve and display data
print("User ID:", db.get('userID'))       # Output: 1002
print("User Score:", db.get('userScore')) # Output: 88

# Start another transaction and rollback
db.begin_transaction()
db.put('userScore', 95)   # Attempt to update user's score
print("User 1002 Score updated to 95, but not committed.")
db.rollback()

# Display data after rollback
print("User Score after rollback:", db.get('userScore')) # Output remains 88
