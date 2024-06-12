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
            couriers_list = cursor.fetchall()
            return couriers_list 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
        
def fetch_orders():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_select_orders = """
                SELECT * FROM orders;
            """
            cursor.execute(sql_select_orders)
            raw_orders = cursor.fetchall()
            orders = []
            for order in raw_orders:
                order_details = {
                    'order_id': order['order_id'],
                    'customer_name': '',
                    'customer_address': '',
                    'customer_phone': '',
                    'courier': order['courier'],  # Matches schema
                    'status': order['status'],  # Matches schema
                    'items': []  # Matches schema
                }
                customer_query = """
                    SELECT * FROM customer_details WHERE customer_id=%s;
                """
                cursor.execute(customer_query, (order['customer_id'],))
                customer = cursor.fetchone()
                if customer:
                    order_details['customer_name'] = customer['customer_name']
                    order_details['customer_address'] = customer['customer_address']
                    order_details['customer_phone'] = customer['customer_phone']
                order_items_query = """
                    SELECT * FROM items WHERE order_id=%s;  # Matches schema
                """
                cursor.execute(order_items_query, (order['order_id'],))
                order_items = cursor.fetchall()
                for item in order_items:
                    product_query = """
                        SELECT * FROM products WHERE product_id=%s;
                    """
                    cursor.execute(product_query, (item['product_id'],))
                    product = cursor.fetchone()
                    if product:
                        ordered_item = {
                            'product_id': item['product_id'],
                            'product_name': product['name'],
                            'quantity': item['quantity']
                        }
                        order_details['items'].append(ordered_item)  # Matches schema
                orders.append(order_details)
            return orders 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()





def fetch_statuses():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql_select_orders = "SELECT * FROM order_statuses"
            cursor.execute(sql_select_orders)
            statuses_list = cursor.fetchall()
            return statuses_list
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

# def insert_product(products):
#     try:
#         connection = get_db_connection()
#         with connection.cursor() as cursor:
#             sql_insert_product = "INSERT INTO products (name, price) VALUES (%s, %s)"
#             for product in products:
#                 cursor.execute(sql_insert_product, (product["name"], product["price"]))
#             connection.commit()
#     except pymysql.Error as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()

# def insert_courier(couriers):
#     try:
#         connection = get_db_connection()
#         with connection.cursor() as cursor:
#             sql_insert_courier = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
#             for courier in couriers:
#                 cursor.execute(sql_insert_courier, (courier["name"], courier["phone"]))
#             connection.commit()
#     except pymysql.Error as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()

def create_product(name, price):
    price = float(price)
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

def create_courier(name, phone):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_insert = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
            cursor.execute(sql_insert, (name, phone))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def create_order(customer_name,customer_address,customer_phone,courier,status,items):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_insert = "INSERT INTO orders (customer_name,customer_address,customer_phone,courier,status,items) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_insert, (customer_name,customer_address,customer_phone,courier,status,items))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def update_product_price(product_id, price):
    try:
        price = float(price)
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_update = "UPDATE products SET price = %s WHERE product_id = %s"
            cursor.execute(sql_update, (price, product_id))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
 
def update_courier_phone(courier_id, phone):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_update = "UPDATE couriers SET phone = %s WHERE courier_id = %s"
            cursor.execute(sql_update, (phone, courier_id))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
 
def update_product_name(product_id, name):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_update = "UPDATE products SET name = %s WHERE product_id = %s"
            cursor.execute(sql_update, (name, product_id))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def update_courier_name(courier_id, name):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_update = "UPDATE couriers SET name = %s WHERE courier_id = %s"
            cursor.execute(sql_update, (name, courier_id))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def update_table_value(table, column, value, id_column, id_value):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_update = f"UPDATE {table} SET {column} = %s WHERE {id_column} = %s"
            cursor.execute(sql_update, (value, id_value))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def delete_product(product_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_delete = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql_delete, (product_id))
            connection.commit()
            print("Product deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def delete_courier(courier_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_delete = "DELETE FROM couriers WHERE courier_id = %s"
            cursor.execute(sql_delete, (courier_id))
            connection.commit()
            print("Courier deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def delete_order(order_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_delete = "DELETE FROM orders WHERE order_id = %s"
            cursor.execute(sql_delete, (order_id,))
            connection.commit()
            print(f"Order with ID {order_id} has been deleted.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def delete_order_and_records(order_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql_delete_items = "DELETE FROM items WHERE order_id = %s"
            cursor.execute(sql_delete_items, (order_id,))
            
            sql_delete_order = "DELETE FROM orders WHERE order_id = %s"
            cursor.execute(sql_delete_order, (order_id,))
            
            sql_delete_customer = """
                DELETE FROM customer_details WHERE customer_id = (
                    SELECT customer_id FROM orders WHERE order_id = %s
                )
            """
            cursor.execute(sql_delete_customer, (order_id,))
            
            connection.commit()
            print(f"Order {order_id} and associated records deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
