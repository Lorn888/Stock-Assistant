def products_menu(products_list):
    product_menu_options = [
    "0-Return to the Main Menu",
    "1-Products List",
    "2-Create New Product",
    "3-Update EXisting Product",
    "4-Delete Product",
]
    while True:
        # PRINT product menu options
        print(product_menu_options)
        # GET user input for product menu option
        product_menu_input = int(input("Chose from above product menu"))

        if product_menu_input == 0:
            # RETURN to main menu
            break

        elif product_menu_input == 1:
            # PRINT products list
            print(products_list)

        elif product_menu_input == 2:
            # GET user input for product name
            new_product_input = input("type the name of the new product")
            # GET user input for product price
            new_product_price_input = float(
                input("type the price of the new product")
            )
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
                print(f"{products_list.index(product)}-{product}")
            # GET user input for product index value
            product_to_update_input = int(input("Chose the product to update"))

            for i in products_list[product_to_update_input]:
                # GET user input for updated property
                user_input = input(i)
                if len(user_input) <= 0:
                    # do not update this property and skip
                        products_list[product_to_update_input][i] = products_list[product_to_update_input][i]
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
            product_to_delete = int(input("Chose the product to delete"))
            # DELETE product at index in products list
            products_list.remove(products_list[product_to_delete])
            print(products_list)
