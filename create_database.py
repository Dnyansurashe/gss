import sqlite3

def create_db():
    # Connect to SQLite database (will create database.db if it doesn't exist)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the Products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
    )
    ''')

    # Insert sample data into the Products table
    cursor.executemany('''
    INSERT INTO Products (name, price, description)
    VALUES (?, ?, ?)
    ''', [
        # Vegetables
        ('Carrot', 1.75, 'Crunchy orange carrots'),
        ('Broccoli', 2.75, 'Healthy green broccoli'),
        ('Spinach', 1.30, 'Fresh spinach leaves'),
        ('Potato', 0.75, 'Versatile potatoes'),
        ('Onion', 1.25, 'Crisp onions'),
        ('Cabbage', 2.50, 'Crunchy green cabbage'),
        ('Bell Pepper', 1.50, 'Colorful bell peppers'),
        
        # Fruits
        ('Apple', 0.99, 'Fresh red apples'),
        ('Banana', 0.59, 'Ripe yellow bananas'),
        ('Orange', 1.00, 'Juicy oranges'),
        ('Strawberry', 3.20, 'Sweet strawberries'),
        ('Blueberry', 4.00, 'Fresh blueberries'),
        ('Avocado', 2.00, 'Creamy avocados'),
        ('Lemon', 1.00, 'Tangy yellow lemons'),
        
        # Dairy Products
        ('Milk', 1.20, 'Fresh whole milk'),
        ('Cheese', 3.80, 'Sharp cheddar cheese'),
        ('Yogurt', 1.50, 'Greek yogurt'),
        ('Butter', 2.70, 'Creamy unsalted butter'),
        ('Eggs', 2.30, 'Organic eggs'),
        
        # Meat
        ('Chicken Breast', 5.99, 'Fresh chicken breasts'),
        ('Ground Beef', 7.50, 'Lean ground beef'),
        ('Pork Chop', 6.00, 'Juicy pork chops'),
        ('Bacon', 4.50, 'Crispy bacon strips'),
        
        # Seafood
        ('Salmon', 12.00, 'Fresh salmon fillets'),
        ('Shrimp', 10.00, 'Large shrimp'),
        ('Tuna', 8.00, 'Tuna steaks'),
        ('Crab', 15.00, 'Fresh crabs'),
        
        # Fast Food
        ('Burger', 5.00, 'Juicy beef burger'),
        ('Pizza', 8.00, 'Cheese pizza'),
        ('Hot Dog', 3.50, 'Classic hot dog'),
        ('French Fries', 2.50, 'Crispy french fries'),
        ('Chicken Nuggets', 4.50, 'Crispy chicken nuggets')
    ])

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print('Database created and populated with sample data.')
