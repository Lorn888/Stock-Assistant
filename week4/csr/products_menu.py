import os

# Clear screen function
def clear_screen():
    os.system('cls')

def print_orders_menu():
    print("===================================")
    print("           PRODUCTS MENU           ")
    print("===================================")
    print("0. Return to the Main Menu")
    print("1. Products List")
    print("2. Create New Product")
    print("3. Update Existing Product")
    print("4. Delete Product")
    print("===================================")

def products_menu(products_list):
    while True:
        # PRINT product menu options
        print_orders_menu()
        # GET user input for product menu option
        product_menu_input = int(input("Please enter your choice (0-4): "))
        clear_screen()
        if product_menu_input == 0:
            # RETURN to main menu
            break

        elif product_menu_input == 1:
            # PRINT products list
            
            for product in products_list:
                print (product)
                print("-----------")

        elif product_menu_input == 2:
            # GET user input for product name
            print("===================================")
            new_product_input = input("type the name of the new product or press Enter: ")
            # GET user input for product price
            print("===================================")
            new_product_price_input = float(input("type the price of the new product or press Enter: "))
            # CREATE new product dictionary with above properties
            new_product = {
                "name": new_product_input,
                "price": new_product_price_input,
            }
            # APPEND product dictionary to products list
            products_list.append(new_product)

        elif product_menu_input == 3:

            # PRINT product names with its index value
            for product in products_list:
                print("-----------")
                print(f"{products_list.index(product)}-{product}")
            # GET user input for product index value
            print("===================================")
            product_to_update_input = int(input("Chose the product to update: "))

            for i in products_list[product_to_update_input]:
                # GET user input for updated property
                print("===================================")
                user_input = input(f"{i}: ")
                if len(user_input) <= 0:
                    # do not update this property and skip
                    products_list[product_to_update_input][i] = products_list[
                        product_to_update_input
                    ][i]
                else:
                    if i == "price":
                        user_input = float(user_input)
                    # update the property value with user input
                    products_list[product_to_update_input][i] = user_input

        elif product_menu_input == 4:
            # PRINT products list
            for product in products_list:
                print(f"{products_list.index(product)}-{product}")
            # GET user input for product index value
            print("===================================")
            product_to_delete = int(input("Chose the product to delete: "))
            # DELETE product at index in products list
            products_list.remove(products_list[product_to_delete])
            print(products_list)
