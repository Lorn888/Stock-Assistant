import os
import csv

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
    print("0. Exit")
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