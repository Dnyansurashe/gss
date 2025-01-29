import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Get the structure of the Products table
cursor.execute("PRAGMA table_info(Products)")
columns = cursor.fetchall()
conn.close()

# Display the column names
print("Products table structure:")
for col in columns:
    print(col)
