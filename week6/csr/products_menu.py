from helper_functions import *
from db_functions import *


def products_menu():
    while True:
        clear_screen()
        print_products_menu()
        product_menu_input = get_number_input(
            "Please enter your choice (0-4): ", "number", 4, True
        )
        clear_screen()
        # Return to the main manu
        if product_menu_input == 0:
            break
        # Products List
        elif product_menu_input == 1:
            products_list = fetch_products()
            if len(products_list) == 0:
                input("Products list is empty\nPress Enter to return")
            else:
                for product in products_list:
                    print(
                        f"{product['name']} - £{product['price']} | {product['quantity']} units"
                    )
                    print("-----------")
                input("Press enter to return to the Products Menu")
        # Create new product
        elif product_menu_input == 2:
            # GET user input for product name
            print("===================================")
            new_product_input = input(
                "type the name of the new product or press Enter to return to Products Menu: "
            )
            if new_product_input:
                print("===================================")
                new_product_price_input = get_number_input(
                    "type the price of the new product or press Enter to cancel and return to Products Menu: ",
                    "number",
                    None,
                    True,
                )
                if new_product_price_input:
                    print("===================================")
                    new_product_quantity_input = get_number_input(
                        "type the quantity of the new product or press Enter to cancel and return to Products Menu: ",
                        "number",
                        None,
                        True,
                    )

                if new_product_price_input is not "":
                    create_product(
                        new_product_input,
                        new_product_price_input,
                        new_product_quantity_input,
                    )
                else:
                    continue
            else:
                continue
        # Update Existing Product
        elif product_menu_input == 3:
            products_list = fetch_products()
            if len(products_list) == 0:
                input("There is nothing to update!\nPress Enter to return")
            else:
                for product in products_list:
                    print("-----------")
                    print(
                        f"{product['product_id']}: {product['name']} - £{product['price']} | {product['quantity']} units"
                    )
                print("===================================")

                while True:
                    product_to_update_input = get_number_input(
                        "Choose the product to update or press Enter to return to Products Menu: ",
                        "number",
                        None,
                        True,
                    )
                    if product_to_update_input == "":
                        break

                    product_to_update_input = int(product_to_update_input)
                    indexes = [product["product_id"] for product in products_list]

                    if product_to_update_input not in indexes:
                        print("That product id is not available")
                        continue
                    else:
                        for product in products_list:
                            if product["product_id"] == product_to_update_input:
                                for key in product:
                                    if key == "product_id":
                                        continue
                                    else:
                                        print("===================================")
                                        user_input = input(
                                            f"Type new {key} or press Enter to skip: "
                                        )
                                        if len(user_input) == 0:
                                            continue
                                        elif key == "price":
                                            while True:
                                                if user_input == "":
                                                    break
                                                try:
                                                    number = float(user_input)
                                                    if number < 0:
                                                        print(
                                                            "Error: Price cannot be negative."
                                                        )
                                                    else:
                                                        update_product_price(
                                                            product_to_update_input,
                                                            number,
                                                        )
                                                        break
                                                except ValueError:
                                                    print("Error: Wrong price.")
                                                user_input = input(
                                                    "Please enter a valid price or press Enter to skip: "
                                                )
                                        elif key == "quantity":
                                            while True:
                                                if user_input == "":
                                                    break
                                                try:
                                                    number = int(user_input)
                                                    if number < 0:
                                                        print(
                                                            "Error: Quantity cannot be negative (stock check recomended)"
                                                        )
                                                    else:
                                                        update_product_quantity(
                                                            product_to_update_input,
                                                            number,
                                                        )
                                                        break
                                                except ValueError:
                                                    print("Error: Wrong quantity.")
                                                user_input = input(
                                                    "Please enter a valid quantity or press Enter to skip: "
                                                )
                                        else:
                                            update_product_name(
                                                product_to_update_input, user_input
                                            )
                        break
        # Delete Product
        elif product_menu_input == 4:

            products_list = fetch_products()
            if len(products_list) == 0:
                input("There is nothing to delete!\nPress Enter to return")
            else:
                for product in products_list:
                    print("-----------")
                    print(
                        f"{product['product_id']}: {product['name']} - £{product['price']}"
                    )
                print("===================================")

                while True:
                    product_to_delete = get_number_input(
                        "Choose the product to delete or press Enter to go back to Products Menu: ",
                        "number",
                        None,
                        True,
                    )
                    if product_to_delete == "":
                        break

                    product_to_delete = int(product_to_delete)
                    indexes = [product["product_id"] for product in products_list]

                    if product_to_delete not in indexes:
                        print("That product id is not available")
                        continue
                    else:
                        delete_product(product_to_delete)
                        print(f"Product with ID {product_to_delete} has been deleted.")
                        break
