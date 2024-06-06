import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables for database connection
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

try:
    # Establish a database connection
    with pymysql.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password) as connection:

        # Create a cursor object to execute SQL queries
        with connection.cursor() as cursor:
            # Inserting a new record into the couriers table
            sql_insert_courier = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
            courier_data = ("Tomek", "0789887889")
            cursor.execute(sql_insert_courier, courier_data)
            connection.commit()

            # Inserting a new record into the products table
            sql_insert_product = "INSERT INTO products (name, price) VALUES (%s, %s)"
            product_data = ("coke-zero", "0.6")
            cursor.execute(sql_insert_product, product_data)
            connection.commit()

            # Example: Selecting records from a table (just for verification)
            sql_select_products = "SELECT * FROM products"
            cursor.execute(sql_select_products)
            products_result = cursor.fetchall()

            print("Products table:")
            for row in products_result:
                print(row)

            sql_select_couriers = "SELECT * FROM couriers"
            cursor.execute(sql_select_couriers)
            couriers_result = cursor.fetchall()

            print("Couriers table:")
            for row in couriers_result:
                print(row)

except pymysql.Error as e:
    # Handle any database errors
    print(f"Error: {e}")
