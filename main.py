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
SELECT employees.firstName, employees.lastName, employees.jobTitle 
FROM employees
JOIN offices
ON employees.officeCode = offices.officeCode
WHERE offices.city = 'Boston';
""", conn
).head()

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql(
    """
SELECT * 
FROM offices
LEFT JOIN employees
ON employees.officeCode = offices.officeCode
WHERE employees.employeeNumber IS NULL;
""", conn
)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql(
    """
SELECT employees.firstName, employees.lastName, offices.city, offices.state
FROM employees
LEFT JOIN offices
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
""", conn
)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql(
    """
SELECT customers.contactFirstName, customers.contactLastName, payments.amount, payments.paymentDate
FROM customer
LEFT JOIN payments
ORDER BY payments.amount DESC;
""", conn
)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql(
    """
SELECT employees.employeeNumber, employees.firstName, employees.lastName, customers.customerNumber, customers.creditLimit
FROM customers
LEFT JOIN employees
ON employees.employeeNumber = customers.salesRepEmployeeNumber
GROUP BY customers.creditLimit
ORDER BY customers.customerNumber DESC
LIMIT 4;
""", conn
)

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql(
    """
SELECT customers.customerName AS n_customers, offices.officeCode, offices.city
FROM customers
JOIN customers
ORDER BY offices.officeCode;
""", conn
)

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql(
    """
SELECT employeeNumber, firstName, lastName
FROM emloyees
WHERE officeCode IN (
SELECT officeCode 
FROM offices
GROUP BY employeeNumber
HAVING COUNT(officeCode) <20
);
""", conn
)

conn.close()
