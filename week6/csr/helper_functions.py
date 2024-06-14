import os
import csv

order_status = ["PREPARING", "READY", "SHIPPED"]

def group_by_key_value(data_list, key):
    grouped_dict = {}
    for dictionary in data_list:
        if dictionary[key] not in grouped_dict:
            grouped_dict[dictionary[key]] = [dictionary]
        else:
            grouped_dict[dictionary[key]].append(dictionary)
    return grouped_dict

def get_number_input(prompt, input_type="number", index=None, allow_empty=False):
    while True:
        user_input = input(prompt)
        
        if allow_empty and user_input == "":
            return ""  

        if input_type == "number":
            try:
                number = float(user_input)
                if number.is_integer():
                    number = int(number)
                if index is not None and (number < 0 or number > index):
                    print(f"Error: Please enter a number between 0 and {index}.")
                else:
                    return number
            except ValueError:
                print("Error: Please enter a valid number.")
        elif input_type == "string":
            return user_input
        elif input_type == "phone":
            if user_input.isdigit() or (allow_empty and user_input == ""):
                return user_input
            else:
                print("Error: Please enter a valid phone number.")
        else:
            print("Error: Invalid input type specified.")

def clear_screen():
    os.system('cls')

def load_data_from_csv(file_path): 
    data = []
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except Exception as e:
        print(e)
    return data

def save_data_to_csv(file_path, data, header):
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(e)
      
def print_main_menu():
    print("===================================")
    print("||          MAIN MENU            ||")
    print("===================================")
    print("0. Exit and Save Changes")
    print("1. Products Menu")
    print("2. Couriers Menu")
    print("3. Orders Menu")
    print("===================================")

def print_products_menu():
    print("===================================")
    print("||         PRODUCTS MENU         ||")
    print("===================================")
    print("0. Return to the Main Menu")
    print("1. Products List")
    print("2. Create New Product")
    print("3. Update Existing Product")
    print("4. Delete Product")
    print("===================================")

def print_couriers_menu():
    print("===================================")
    print("||         COURIERS MENU         ||")
    print("===================================")
    print("0. Return to the Main Menu")
    print("1. Print courier list")
    print("2. Create a new Courier")
    print("3. Update Existing Courier")
    print("4. Delete Order")
    print("===================================")

def print_orders_menu():
    print("===================================")
    print("||          ORDERS MENU          ||")
    print("===================================")
    print("0. Return to the Main Menu")
    print("1. Print orders dictionary")
    print("2. Create a new order")
    print("3. Update Existing Order Status")
    print("4. Update Existing Order")
    print("5. Delete Order")
    print("6. Save orders in csv file")
    print("===================================")
