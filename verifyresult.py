# Employees
employees_df = pd.DataFrame(list(mongo_db.employees.find()))
employees_df.head()

# Offices
offices_df = pd.DataFrame(list(mongo_db.offices.find()))
offices_df.head()


# Customers (nested 'payments' and 'salesRep' will be embedded dicts/lists)
customers_df = pd.DataFrame(list(mongo_db.customers.find()))
customers_df[['customerNumber', 'customerName', 'payments']].head()

# Orders (nested 'orderDetails' will be lists of dicts)
orders_df = pd.DataFrame(list(mongo_db.orders.find()))
orders_df[['orderNumber', 'orderDate', 'orderDetails']].head()


# Products
products_df = pd.DataFrame(list(mongo_db.products.find()))
products_df.head()

# Product Lines (with embedded products)
productlines_df = pd.DataFrame(list(mongo_db.productlines.find()))
productlines_df[['productLine', 'products']].head()
