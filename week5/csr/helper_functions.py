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

def get_number_input(prompt, index="no", empty="empty"):
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
                    if index is not "no":
                        if 0 <= number <= index:
                            return number
                        else:
                            print("Out of scope")
                    else:
                        return number

                else:
                    return user_input
                  # Return the number if input is valid
        except ValueError:
            print("Error: Please enter a valid number.")


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
    print("===================================")
