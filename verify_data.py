import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Query all rows in the Products table
cursor.execute("SELECT * FROM Products")
rows = cursor.fetchall()
conn.close()

# Display all products in the table
if rows:
    print("Products in database:")
    for row in rows:
        print(row)
else:
    print("No data found in Products table.")
