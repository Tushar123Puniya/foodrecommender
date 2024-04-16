import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Execute SQL query to delete all rows from the users table
cursor.execute('DELETE FROM users')

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Users table cleared successfully.")
