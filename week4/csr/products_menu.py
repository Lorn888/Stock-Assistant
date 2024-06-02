from helper_functions import get_number_input, clear_screen, print_products_menu

def products_menu(products_list):
    while True:
        clear_screen()
        # PRINT product menu options
        print_products_menu()
        # GET user input for product menu option
        product_menu_input = get_number_input("Please enter your choice (0-4): ",4)
        clear_screen()
        if product_menu_input == 0:
            # RETURN to main menu
            break

        elif product_menu_input == 1:
            # PRINT products list
            if len(products_list) == 0:
                input("Products list is empty\nPress Enter to return")
            else:
                for product in products_list:
                    print (product)
                    print("-----------")
                input("Press enter to return to the Products Menu")
            
        elif product_menu_input == 2:
            # GET user input for product name
            print("===================================")
            new_product_input = input("type the name of the new product or press Enter to return to Products Menu: ")
            if new_product_input:
                # GET user input for product price
                print("===================================")
                new_product_price_input = get_number_input("type the price of the new product or press Enter to cancel and return to Products Menu: ")
                if new_product_price_input is not "":

                # CREATE new product dictionary with above properties
                    new_product = {
                        "name": new_product_input,
                        "price": float(new_product_price_input)
                }
                # APPEND product dictionary to products list
                    products_list.append(new_product)
                else:
                    continue
            else:
                continue

        elif product_menu_input == 3:
            if len(products_list) == 0:
                input("there is nothing to update!\nPress Enter to return")
            else:
            # PRINT product names with its index value
                for product in products_list:
                    print("-----------")
                    print(f"{products_list.index(product)}-{product}")
                # GET user input for product index value
                print("===================================")
                product_to_update_input = get_number_input("Chose the product to update or press Enter to retrn to Products Menu: "(len(products_list)-1))
                if product_to_update_input is not "":
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
                else:
                    continue

        elif product_menu_input == 4:
            # PRINT products list
            if len(products_list) == 0:
                input("there is nothing to delete!\nPress Enter to return")
            else:
                for product in products_list:
                    print("-----------")
                    print(f"{products_list.index(product)}-{product}")
            # GET user input for product index value
                print("===================================")
                product_to_delete = get_number_input("Chose the product to delete or press Enter to go back to Products Menu: ",(len(products_list)-1))
                if product_to_delete is not "":
            # DELETE product at index in products list
                    products_list.remove(products_list[product_to_delete])
                else:
                    continue
            
