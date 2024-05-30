from products_menu import products_menu
from couriers_menu import couriers_menu
from orders_menu import orders_menu

import csv

def load_data_from_csv(file_path):
    data = []
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except Exception as e:
        print(e)
    return data

# Define file paths
products_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/products.csv"
couriers_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/couriers.csv"
orders_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/orders.csv"

# Load data from CSV files
products_list = load_data_from_csv(products_file_path)
couriers_list = load_data_from_csv(couriers_file_path)
orders_list = load_data_from_csv(orders_file_path)


# CREATE order status list
order_status = ["PREPARING", "READY", "SHIPPED"]

main_menu_options = ["0-Exit App", "1-Product Menu", "2-Couriers Menu", "3-Orders Menu"]



while True:
    # PRINT main menu options
    print(main_menu_options)
    # GET user input for main menu option
    main_menu_input = int(input("Chose from the above 3 options '0-3'"))

    if main_menu_input == 0:
        # SAVE products list to products.csv
        def save_data_to_csv(file_path, data, header):
            try:
                with open(file_path, "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=header)
                    writer.writeheader()
                    for row in data:
                        writer.writerow(row)
            except Exception as e:
                print(e)

        # Define header for each CSV file
        products_header = ["name", "price"]
        couriers_header = ["name", "phone"]
        orders_header = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

        # Define file paths
        products_file_path = "week4/data/products.csv"
        couriers_file_path = "week4/data/couriers.csv"
        orders_file_path = "week4/data/orders.csv"

        # Save data to CSV files
        save_data_to_csv(products_file_path, products_list, products_header)
        save_data_to_csv(couriers_file_path, couriers_list, couriers_header)
        save_data_to_csv(orders_file_path, orders_list, orders_header)
        # EXIT app
        break

    # Product Menu
    elif main_menu_input == 1:
        products_menu(products_list)
        
    # Couriers Menu
    elif main_menu_input == 2:
        couriers_menu(couriers_list)

    # Orders Menu
    elif main_menu_input == 3:
        orders_menu(orders_list,order_status,couriers_list, products_list)