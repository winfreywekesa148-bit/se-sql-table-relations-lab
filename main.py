# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql(
    """
SELECT firstName, lastName, jobTitle 
FROM employees;
""", conn
).head()

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql(
    """
SELECT * 
FROM employees
FULL JOIN offices
ON employees.officeCode = offices.officeCode
WHERE employees = 'NULL';
""", conn
)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql(
    """
SELECT employees.firstName, employees.lastName, offices.city, offices.state
FROM employees
JOIN employees
ON employees.officeCode = offices.officeCode
ORDER BY employees.firstName, employees.lastName;
""", conn
)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql(
    """
SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
FROM customers
WHERE orderNumber IN (
SELECT orderNumber
FROM orders
GROUP BY orderNumber
WHERE orderNumber = 'NULL'
);
"""
)

# STEP 5
# Replace None with your code
df_payment = None

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()
