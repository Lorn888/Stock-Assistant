import os

# Clear screen function
def clear_screen():
    os.system('cls')

def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number  # Return the number if input is valid
        except ValueError:
            print("Error: Please enter a valid number.")

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

def print_orders_menu():
    print("===================================")
    print("||         PRODUCTS MENU         ||")
    print("===================================")
    print("0. Return to the Main Menu")
    print("1. Products List")
    print("2. Create New Product")
    print("3. Update Existing Product")
    print("4. Delete Product")
    print("===================================")

def products_menu(products_list):
    while True:
        clear_screen()
        # PRINT product menu options
        print_orders_menu()
        # GET user input for product menu option
        product_menu_input = get_number_input("Please enter your choice (0-4): ")
        clear_screen()
        if product_menu_input == 0:
            # RETURN to main menu
            break

        elif product_menu_input == 1:
            # PRINT products list
            
            for product in products_list:
                print (product)
                print("-----------")
            input("Press enter to return to the Products Menu")
        elif product_menu_input == 2:
            # GET user input for product name
            print("===================================")
            while True:
                new_product_input = input("type the name of the new product: ")
                if new_product_input:
                    break
                else:
                    print("This field can not be left empty")
            clear_screen()
            # GET user input for product price
            print("===================================")
            new_product_price_input = get_lol_input("type the price of the new product: ","not empty")
            # CREATE new product dictionary with above properties
            new_product = {
                "name": new_product_input,
                "price": new_product_price_input,
            }
            # APPEND product dictionary to products list
            products_list.append(new_product)

        elif product_menu_input == 3:
            if len(products_list) == 0:
                input("there is nothing to update!")
            else:
            # PRINT product names with its index value
                for product in products_list:
                    print("-----------")
                    print(f"{products_list.index(product)}-{product}")
                # GET user input for product index value
                print("===================================")
                product_to_update_input = get_number_input("Chose the product to update: ")

                for i in products_list[product_to_update_input]:
                    # GET user input for updated property
                    print("===================================")
                    user_input = input(f"Type new {i}\nOr press Enter to skip: ")
                    if len(user_input) <= 0:
                        # do not update this property and skip
                        continue
                    elif i == "price":
                        while True:
                            try:
                                number = int(user_input)
                                products_list[product_to_update_input][i] = float(number)
                                break
                            except ValueError:
                                user_input = input("Please enter a valid number or press Enter to skip: ")
                               
                    else:
                        products_list[product_to_update_input][i] = user_input


        elif product_menu_input == 4:
            # PRINT products list
            if len(products_list) == 0:
                input("there is nothing to delete!")
            else:
                for product in products_list:
                    print("-----------")
                    print(f"{products_list.index(product)}-{product}")
            # GET user input for product index value
                print("===================================")
                product_to_delete = get_number_input("Chose the product to delete: ")
            # DELETE product at index in products list
                products_list.remove(products_list[product_to_delete])
