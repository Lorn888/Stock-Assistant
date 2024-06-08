import pymysql
from db_connection import get_db_connection

def fetch_products():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_select_products = "SELECT * FROM products"
            cursor.execute(sql_select_products)
            products_list = cursor.fetchall()
            return products_list
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def fetch_couriers():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_select_couriers = "SELECT * FROM couriers"
            cursor.execute(sql_select_couriers)
            couriers_result = cursor.fetchall()
            return list(couriers_result) 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
        
def clear_table(table_name):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_clear_table = f"TRUNCATE TABLE {table_name}"
            cursor.execute(sql_clear_table)
            connection.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def insert_product(products):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_insert_product = "INSERT INTO products (name, price) VALUES (%s, %s)"
            for product in products:
                cursor.execute(sql_insert_product, (product["name"], product["price"]))
            connection.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def insert_courier(couriers):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_insert_courier = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
            for courier in couriers:
                cursor.execute(sql_insert_courier, (courier["name"], courier["phone"]))
            connection.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def create_product(name, price):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_insert = "INSERT INTO products (name, price) VALUES (%s, %s)"
            cursor.execute(sql_insert, (name, price))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()