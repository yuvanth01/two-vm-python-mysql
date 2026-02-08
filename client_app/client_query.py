import mysql.connector
import os

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_CLIENT_USER"),
    password=os.getenv("DB_CLIENT_PASSWORD"),
    database="companydb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

conn.close()
