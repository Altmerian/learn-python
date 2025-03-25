import sqlite3


with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        cust_id TEXT PRIMARY KEY,
        cust_name TEXT NOT NULL,
        address TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        prod_no TEXT PRIMARY KEY,
        prod_name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_no INTEGER,
        cust_id TEXT NOT NULL,
        prod_no TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        PRIMARY KEY (order_no, prod_no),
        FOREIGN KEY (cust_id) REFERENCES customer (cust_id),
        FOREIGN KEY (prod_no) REFERENCES product (prod_no)
    )
    ''')
    
    # Check if customer table is empty before inserting data
    cursor.execute("SELECT COUNT(*) FROM customer")
    if cursor.fetchone()[0] == 0:
        # Insert data into customer table
        customers = [
            ('C101', 'Anita', 'Delhi'),
            ('C102', 'Raj', 'Hyderabad'),
            ('C103', 'Michael', 'Kolkata'),
            ('C107', 'Ali', 'Delhi'),
            ('C109', 'Sharma', 'Chennai')
        ]
        cursor.executemany("INSERT INTO customer VALUES (?, ?, ?)", customers)
        print("Customer data inserted.")
    
    # Check if product table is empty before inserting data
    cursor.execute("SELECT COUNT(*) FROM product")
    if cursor.fetchone()[0] == 0:
        # Insert data into product table
        products = [
            ('P10', 'Toothpaste', 20),
            ('P11', 'Toothbrush', 10),
            ('P12', 'Lotion', 30),
            ('P13', 'Shampoo', 25),
            ('P14', 'Soap', 10)
        ]
        cursor.executemany("INSERT INTO product VALUES (?, ?, ?)", products)
        print("Product data inserted.")
    
    # Check if orders table is empty before inserting data
    cursor.execute("SELECT COUNT(*) FROM orders")
    if cursor.fetchone()[0] == 0:
        # Insert data into orders table
        orders = [
            (10005, 'C101', 'P10', 1),
            (10005, 'C101', 'P11', 2),
            (12389, 'C109', 'P12', 1),
            (12389, 'C109', 'P14', 1),
            (12389, 'C109', 'P11', 2),
            (63017, 'C103', 'P13', 4),
            (63017, 'C103', 'P10', 1),
            (63017, 'C103', 'P11', 4),
            (71222, 'C101', 'P12', 2),
            (71222, 'C101', 'P13', 1),
            (96351, 'C102', 'P14', 1)
        ]
        cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)
        print("Order data inserted.")
    
    # Commit changes
    conn.commit()
    
    print("Database setup completed.\n")
    
    # Execute the 10 queries from the image
    print("Query 1: Find all Customers")
    query1 = "SELECT * FROM customer"
    for row in cursor.execute(query1):
        print(row)
    
    print("\nQuery 2: Find all Customers from Delhi")
    query2 = "SELECT * FROM customer WHERE address = 'Delhi'"
    for row in cursor.execute(query2):
        print(row)
    
    print("\nQuery 3: Find all Products with price greater than 20")
    query3 = "SELECT * FROM product WHERE price > 20"
    for row in cursor.execute(query3):
        print(row)
    
    print("\nQuery 4: Find Names of the Products starting with letter 'S'")
    query4 = "SELECT prod_name FROM product WHERE prod_name LIKE 'S%'"
    for row in cursor.execute(query4):
        print(row[0])
    
    print("\nQuery 5: Find Names of Customers either living in Delhi or Chennai")
    query5 = "SELECT cust_name FROM customer WHERE address IN ('Delhi', 'Chennai')"
    for row in cursor.execute(query5):
        print(row[0])
    
    print("\nQuery 6: Find Order No and Product Number with Quantity greater than 1")
    query6 = "SELECT order_no, prod_no FROM orders WHERE quantity > 1"
    for row in cursor.execute(query6):
        print(row)
    
    print("\nQuery 7: Find Name of the Customer with Order number 10005")
    query7 = """
    SELECT DISTINCT c.cust_name 
    FROM customer c
    JOIN orders o ON c.cust_id = o.cust_id
    WHERE o.order_no = 10005
    """
    for row in cursor.execute(query7):
        print(row[0])
    
    print("\nQuery 8: Find Product Names and Quantity in Order number 63017")
    query8 = """
    SELECT p.prod_name, o.quantity
    FROM product p
    JOIN orders o ON p.prod_no = o.prod_no
    WHERE o.order_no = 63017
    """
    for row in cursor.execute(query8):
        print(row)
    
    print("\nQuery 9: Find Order numbers which contains Toothpaste")
    query9 = """
    SELECT DISTINCT o.order_no
    FROM orders o
    JOIN product p ON o.prod_no = p.prod_no
    WHERE p.prod_name = 'Toothpaste'
    """
    for row in cursor.execute(query9):
        print(row[0])
    
    print("\nQuery 10: Find Names of the Customers who purchased Lotion")
    query10 = """
    SELECT DISTINCT c.cust_name
    FROM customer c
    JOIN orders o ON c.cust_id = o.cust_id
    JOIN product p ON o.prod_no = p.prod_no
    WHERE p.prod_name = 'Lotion'
    """
    for row in cursor.execute(query10):
        print(row[0])
    
    
    