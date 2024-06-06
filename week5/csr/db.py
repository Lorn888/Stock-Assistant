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
            # Example: Inserting a new record into a table
            sql_insert = "INSERT INTO `order` (customer_name, customer_address, courier, `status`, items) VALUES (%s, %s, %s, %s, %s)"
            data = ("John", "Unit 2, 12 Main Street, LONDON, WH1 2ER", "0789887334", "2", "PREPARING")
            cursor.execute(sql_insert, data)
            connection.commit()

            # Example: Selecting records from a table
            sql_select = "SELECT * FROM `order`"
            cursor.execute(sql_select)
            result = cursor.fetchall()

            # Process the query result
            for row in result:
                print(row)

except pymysql.Error as e:
    # Handle any database errors
    print(f"Error: {e}")
