from helper_functions import get_number_input, clear_screen, print_products_menu
from db_operation import fetch_products, create_product  , update_product_price, update_product_name, delete_product

def products_menu():
    while True:
        clear_screen()
        # PRINT product menu options
        print_products_menu()
        # GET user input for product menu option
        product_menu_input = get_number_input("Please enter your choice (0-4): ","number", 4, True)
        clear_screen()
        if product_menu_input == 0:
            # RETURN to main menu
            break

        elif product_menu_input == 1:
            products_list = fetch_products()
            # PRINT products list
            if len(products_list) == 0:
                input("Products list is empty\nPress Enter to return")
            else:
                for product in products_list:
                    print (f"{product['name']} - £{product['price']}")
                    print("-----------")
                input("Press enter to return to the Products Menu")
            
        elif product_menu_input == 2:
            # GET user input for product name
            print("===================================")
            new_product_input = input("type the name of the new product or press Enter to return to Products Menu: ")
            if new_product_input:
                # GET user input for product price
                print("===================================")
                new_product_price_input = get_number_input("type the price of the new product or press Enter to cancel and return to Products Menu: ", "number", None, True)
                if new_product_price_input is not "":
                    create_product(new_product_input, new_product_price_input)
         
                else:
                    continue
            else:
                continue

        elif product_menu_input == 3:
            products_list = fetch_products()
            if len(products_list) == 0:
                input("There is nothing to update!\nPress Enter to return")
            else:
                # PRINT product names with their index value
                for product in products_list:
                    print("-----------")
                    print(f"{product['product_id']}: {product['name']} - £{product['price']}")
                # GET user input for product index value
                print("===================================")
                product_to_update_input = get_number_input(
                    "Choose the product to update or press Enter to return to Products Menu: ",
                    "number",
                    len(products_list),
                    True
                )
                if product_to_update_input != "":
                    product_to_update_input = int(product_to_update_input)
                    for i in products_list[product_to_update_input - 1]:
                        if i == 'product_id':
                            continue
                        else:
                            print("===================================")
                            user_input = input(f"Type new {i} or press Enter to skip: ")
                            if len(user_input) <= 0:
                                continue
                            elif i == "price":
                                while True:
                                    if user_input == "":
                                        break 
                                    try:
                                        number = float(user_input)
                                        if number < 0:
                                            print("Error: Price cannot be negative.")
                                        else:
                                            update_product_price(product_to_update_input, number)
                                            break
                                    except ValueError:
                                        print("Error: Please enter a valid price.")
                                    user_input = input("Please enter a valid price or press Enter to skip: ")
                            else:
                                update_product_name(product_to_update_input, user_input)
                else:
                    continue



        elif product_menu_input == 4:
            # PRINT products list
            products_list = fetch_products()
            if len(products_list) == 0:
                input("there is nothing to delete!\nPress Enter to return")
            else:
                for product in products_list:
                    print("-----------")
                    print(f"{product['product_id']}: {product['name']} - £{product['price']}")
            # GET user input for product index value
                print("===================================")
                product_to_delete = get_number_input("Chose the product to delete or press Enter to go back to Products Menu: ","number",(len(products_list)), True)
                if product_to_delete is not "":
            # DELETE product at index in products list
                    delete_product(product_to_delete)
                else:
                    continue
            
