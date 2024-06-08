from products_menu import products_menu
from couriers_menu import couriers_menu
from orders_menu import orders_menu
from helper_functions import get_number_input, clear_screen,load_data_from_csv, save_data_to_csv, print_main_menu
from db_operation import fetch_couriers, insert_courier, fetch_products


couriers_list = fetch_couriers()

# Headers for each CSV file
products_header = ["name", "price"]
couriers_header = ["name", "phone"]
orders_header = [
    "customer name",
    "customer address",
    "customer phone",
    "courier",
    "status",
    "items",
]

# Paths for each file
products_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/products.csv"
couriers_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/couriers.csv"
orders_file_path = "D:/OneDrive/Desktop/VSCode/DE-PC/Mini-Project-GIT/Patryk-miniproject/data/orders.csv"

# Loading data from CSV files
# products_list = load_data_from_csv(products_file_path)
# couriers_list = load_data_from_csv(couriers_file_path)
orders_list = load_data_from_csv(orders_file_path)


# CREATE order status list
order_status = ["PREPARING", "READY", "SHIPPED"]


clear_screen()

# APP
while True:
    # PRINT main me9nu options
    print_main_menu()
    # GET user input for main menu option
    main_menu_input = get_number_input("Please enter your choice (0-3): ",3)
    clear_screen()
    if main_menu_input == 0:

        # Save data to CSV files
        # save_data_to_csv(products_file_path, products_list, products_header)
        # save_data_to_csv(couriers_file_path, couriers_list, couriers_header)
        # clear_table("products")
        # clear_table("couriers")
        insert_courier(couriers_list)
        save_data_to_csv(orders_file_path, orders_list, orders_header)
        # EXIT app
        break

    # Product Menu
    elif main_menu_input == 1:
        products_menu()

    # Couriers Menu
    elif main_menu_input == 2:
        couriers_menu(couriers_list)

    # Orders Menu
    elif main_menu_input == 3:
        products_list = fetch_products()
        orders_menu(orders_list, order_status, couriers_list, products_list)
