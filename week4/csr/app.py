from products_menu import products_menu
from couriers_menu import couriers_menu
from orders_menu import orders_menu
import csv
import os

def get_number_input(prompt, empty="empty"):
    while True:
        user_input = input(prompt)
        try:
            if empty =="not empty":
                if len(user_input) > 0:
                    number = int(user_input)
                    return number
                else:
                    print("This can not be empty")
            elif empty == "empty":
                if len(user_input) > 0:
                    number = int(user_input)
                    return number
                else:
                    return user_input
                  # Return the number if input is valid
        except ValueError:
            print("Error: Please enter a valid number.")

# Clear screen function
def clear_screen():
    os.system('cls')

# Loading Data function
def load_data_from_csv(file_path):
    data = []
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except Exception as e:
        print(e)
    return data

# Saving Data function
def save_data_to_csv(file_path, data, header):
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(e)

# Headers for each CSV file
products_header = ["name", "price"]
couriers_header = ["name", "phone"]
orders_header = [
    "customer_name",
    "customer_address",
    "customer_phone",
    "courier",
    "status",
    "items",
]

# Paths for each file
products_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/products.csv"
couriers_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/couriers.csv"
orders_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/orders.csv"

# Loading data from CSV files
products_list = load_data_from_csv(products_file_path)
couriers_list = load_data_from_csv(couriers_file_path)
orders_list = load_data_from_csv(orders_file_path)

# CREATE order status list
order_status = ["PREPARING", "READY", "SHIPPED"]

def print_main_menu():
    print("===================================")
    print("||          MAIN MENU            ||")
    print("===================================")
    print("0. Exit")
    print("1. Products Menu")
    print("2. Couriers Menu")
    print("3. Orders Menu")
    print("===================================")

clear_screen()

# APP
while True:
    # PRINT main me9nu options
    print_main_menu()
    # GET user input for main menu option
    main_menu_input = get_number_input("Please enter your choice (0-3): ")
    clear_screen()
    if main_menu_input == 0:

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
        orders_menu(orders_list, order_status, couriers_list, products_list)
