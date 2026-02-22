# --- Migrate Employees (Referenced) ---
migrate_table_to_collection("SELECT * FROM employees", mongo_db.employees)

# --- Migrate Offices (Referenced) ---
migrate_table_to_collection("SELECT * FROM offices", mongo_db.offices)

# --- Migrate Customers and Embed Payments ---
mysql_cursor.execute("SELECT * FROM customers")
customers = mysql_cursor.fetchall()
for customer in customers:
    # Embed payments into customer
    mysql_cursor.execute("SELECT * FROM payments WHERE customerNumber = %s", (customer['customerNumber'],))
    payments = mysql_cursor.fetchall()
    customer['payments'] = payments

    # Embed sales rep name
    mysql_cursor.execute("SELECT lastName, firstName FROM employees WHERE employeeNumber = %s", 
                         (customer['salesRepEmployeeNumber'],))
    rep = mysql_cursor.fetchone()
    if rep:
        customer['salesRep'] = rep

    # Insert sanitized customer document
    mongo_db.customers.insert_one(sanitize_for_mongo(customer))

# --- Migrate Orders and Embed OrderDetails ---
mysql_cursor.execute("SELECT * FROM orders")
orders = mysql_cursor.fetchall()
for order in orders:
    # Embed order details
    mysql_cursor.execute("SELECT * FROM orderdetails WHERE orderNumber = %s", (order['orderNumber'],))
    order_details = mysql_cursor.fetchall()
    order['orderDetails'] = order_details

    mongo_db.orders.insert_one(sanitize_for_mongo(order))

# --- Migrate Products (Referenced) ---
migrate_table_to_collection("SELECT * FROM products", mongo_db.products)

# --- Migrate ProductLines and Embed Products ---
mysql_cursor.execute("SELECT * FROM productlines")
productlines = mysql_cursor.fetchall()
for pl in productlines:
    mysql_cursor.execute("SELECT * FROM products WHERE productLine = %s", (pl['productLine'],))
    products = mysql_cursor.fetchall()
    pl['products'] = products
    mongo_db.productlines.insert_one(sanitize_for_mongo(pl))
