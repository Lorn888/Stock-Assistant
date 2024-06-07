# db_operations.py
from db_connection import get_db_connection

def fetch_products():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_select_products = "SELECT * FROM products"
            cursor.execute(sql_select_products)
            products_result = cursor.fetchall()
            return products_result
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def fetch_couriers():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_select_couriers = "SELECT * FROM couriers"
            cursor.execute(sql_select_couriers)
            couriers_result = cursor.fetchall()
            return couriers_result
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Similarly, you can add functions to insert data or perform other operations
