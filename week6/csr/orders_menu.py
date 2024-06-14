from helper_functions import (
    get_number_input,
    clear_screen,
    print_orders_menu,
)
from db_operation import (
    fetch_products,
    fetch_couriers,
    fetch_orders,
    fetch_statuses,
    create_order,
    update_table_value,
    delete_order_and_records,
)


def orders_menu():

    while True:
        clear_screen()
        print_orders_menu()
        orders_menu_input = get_number_input(
            "Please enter your choice (0-5): ", "number", 5, True
        )
        clear_screen()
        if orders_menu_input == 0:
            #  RETURN to main menu
            break

        elif orders_menu_input == 1:
            orders_list = fetch_orders()
            # PRINT orders dictionary
            if len(orders_list) == 0:
                input("Orders list is empty\nPress Enter to return")
            else:
                for order in orders_list:
                    print(f"Order ID: {order['order_id']}")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Courier ID: {order['courier']}")
                    print(f"Order Status: {order['status']}")
                    print("Items:")
                    for item in order['items']:
                        print(f"    Product Name: {item['product_name']}")
                        print(f"    Quantity: {item['quantity']}")
                        print("    ---------------")
                    print("===============================")
                input("Press enter to return to the Orders Menu")

        elif orders_menu_input == 2:
            print("===================================")
            customer_name_input = input(
                "Insert Customer name or press Enter to return to Orders Menu"
            )
            if customer_name_input:
                customer_address_input = input(
                    "Insert Customer address or press Enter to cancel and return to the Orders Menu"
                )
                if customer_address_input:
                    customer_phone_input = get_number_input(
                        "Insert Customer phone number or press Enter to cancel and return to Orders Menu",
                        "phone",
                        None,
                        True,
                    )
                    if customer_phone_input:
                        products_list = fetch_products()
                        order_items = []
                        while True:
                            for product in products_list:
                                print(
                                    f"{product['product_id']}: {product['name']} - £{product['price']} - {product['quantity']} units available"
                                )

                            prod_index_val_input = get_number_input(
                                "Choose a product or press Enter to cancel and return to Orders Menu: ",
                                "number",
                                None,
                                True,
                            )

                            if not prod_index_val_input:
                                break

                            already_chosen = False
                            for item in order_items:
                                if prod_index_val_input == item["product_id"]:
                                    already_chosen = True
                                    print("You have already chosen this product.")
                                    break

                            if not already_chosen:
                                chosen_product = {
                                    "product_id": prod_index_val_input,
                                    "quantity": None,
                                }
                                product_quantity = None
                                for product in products_list:
                                    if product["product_id"] == prod_index_val_input:
                                        product_quantity = product["quantity"]
                                        print(f"{product_quantity} units available")

                                while True:  # Loop to validate quantity
                                    units = get_number_input(
                                        "How many units?: ", "number", None, False
                                    )
                                    if units == 0:
                                        print(
                                            "Quantity cannot be zero. Please choose again."
                                        )
                                    elif units > product_quantity:
                                        print(
                                            f"Cannot select more than available quantity ({product_quantity} units). Please choose again."
                                        )
                                    else:
                                        chosen_product["quantity"] = units
                                        order_items.append(chosen_product)
                                        break  # Exit the loop if quantity is valid

                                more = input(
                                    "Would you like to choose more products? 'y' for yes, 'n' for no: "
                                )
                                if more.lower() == "n":
                                    break
                                else:
                                    continue

                        if order_items:
                            couriers_list = fetch_couriers()
                            for courier in couriers_list:
                                print(
                                    f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}"
                                )

                            while True:
                                select_courier_input = get_number_input(
                                    "Select a courier", "number", None, True
                                )
                                if select_courier_input == "":
                                    break
                                select_courier_input = int(select_courier_input)
                                indexes = [
                                    courier["courier_id"] for courier in couriers_list
                                ]
                                if select_courier_input not in indexes:
                                    print("Courier with this id is not available")
                                    continue
                                else:
                                    create_order(
                                        customer_name_input,
                                        customer_address_input,
                                        customer_phone_input,
                                        select_courier_input,
                                        1,
                                        order_items,
                                    )  # Create order with customer and product details

                                    # Update the quantity for each product in the order
                                    for item in order_items:
                                        product_id = item["product_id"]
                                        units_ordered = item["quantity"]

                                        # Fetch the current quantity of the product from the database
                                        for product in products_list:
                                            if product["product_id"] == product_id:
                                                product_quantity = product["quantity"]

                                        remaining_quantity = product_quantity - units_ordered
                                        update_table_value(
                                            "products",
                                            "quantity",
                                            remaining_quantity,
                                            "product_id",
                                            product_id,
                                        )  # Update product quantity in the database
                                    break
                        else:
                            print(
                                "No valid product index values provided. Returning to Orders Menu."
                            )
                    else:
                        print("Invalid customer phone number. Returning to Orders Menu.")
                else:
                    print("Invalid customer address. Returning to Orders Menu.")
            else:
                print("Invalid customer name. Returning to Orders Menu.")


        elif orders_menu_input == 3:
            orders_list = fetch_orders()

            # PRINT orders list with its index values
            if len(orders_list) == 0:
                input("There is no orders in the list\nPress Enter to return")
            else:
                for order in orders_list:
                    print(
                        f"Order ID: {order['order_id']}\n"
                        f"Customer Name: {order['customer_name']}\n"
                        f"Customer Address: {order['customer_address']}\n"
                        f"Customer Phone: {order['customer_phone']}\n"
                        f"Courier: {order['courier']}\n"
                        f"Status: {order['status']}\n"
                        f"Items: {order['items']}\n"
                        f"-----------------------------"
                    )

                # GET user input for order index value
                order_status_to_update_input = get_number_input(
                    "Chose the order to update the status of of press Enter to return to Orders Menu",
                    "number",
                    None,
                    True,
                )
                if order_status_to_update_input != "":
                    # PRINT order status list with index values
                    statuses_list = fetch_statuses()
                    for status in statuses_list:
                        print(f"{status['status_id']}: {status['order_status']}")

                    # GET user input for order status index value
                    updated_status_input = get_number_input(
                        "What would you like to update it to? Or press Enter to cancel changes",
                        "number",
                        None,
                        True,
                    )
                    if updated_status_input != "":

                        # UPDATE status for order
                        update_table_value(
                            "orders",
                            "status",
                            updated_status_input,
                            "order_id",
                            order_status_to_update_input,
                        )
                    else:
                        continue
                else:
                    continue

        elif orders_menu_input == 4:
            orders_list = fetch_orders()
            # PRINT orders list with its index values
            if len(orders_list) == 0:
                input("there is nothing to update\nPress Enter to return")
            else:
                for order in orders_list:
                    print(
                        f"Order ID: {order['order_id']}\n"
                        f"Customer Name: {order['customer_name']}\n"
                        f"Customer Address: {order['customer_address']}\n"
                        f"Customer Phone: {order['customer_phone']}\n"
                        f"Courier: {order['courier']}\n"
                        f"Status: {order['status']}\n"
                        f"Items: {order['items']}\n"
                        f"-----------------------------"
                    )
                while True:
                    order_to_update = get_number_input(
                        "Chose order to update or press Enter to return to Orders Menu: ",
                        "number",
                        None,
                        True,
                    )
                    if order_to_update == "":
                        break

                    indexes = [order["order_id"] for order in orders_list]

                    if order_to_update not in indexes:
                        print("That order id is not available")
                        continue
                    else:
                        for i in orders_list[0]:
                            if i == "order_id":
                                continue

                            elif i == "courier":
                                for courier in couriers_list:
                                    print("-----------")
                                    print(
                                        f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}"
                                    )
                                update_input = get_number_input(
                                    f"Type new {i}\nOr press Enter to skip: ",
                                    "number",
                                    None,
                                    True,
                                )
                                if update_input != "":
                                    update_table_value(
                                        "orders",
                                        "courier",
                                        update_input,
                                        "order_id",
                                        order_to_update,
                                    )
                                else:
                                    continue
                            elif i == "status":
                                statuses_list = fetch_statuses()
                                for status in statuses_list:
                                    print("-----------")
                                    print(
                                        f"{status['status_id']}: {status['order_status']}"
                                    )
                                update_input = get_number_input(
                                    f"Type new {i}\nOr press Enter to skip: ",
                                    "number",
                                    None,
                                    True,
                                )
                                if update_input != "":
                                    update_table_value(
                                        "orders",
                                        "status",
                                        update_input,
                                        "order_id",
                                        order_to_update,
                                    )
                                else:
                                    continue
                            elif i == "customer_phone":
                                update_input = get_number_input(
                                    f"Type new {i}\nOr press Enter to skip: ",
                                    "phone",
                                    None,
                                    True,
                                )
                                if update_input != "":
                                    update_table_value(
                                        "customer_details",
                                        "customer_phone",
                                        update_input,
                                        "customer_id",
                                        order_to_update,
                                    )
                                else:
                                    continue
                            else:
                                update_input = input(
                                    f"Type new {i}\nOr press Enter to skip: "
                                )
                                if update_input != "":
                                    update_table_value(
                                        "customer_details",
                                        i,
                                        update_input,
                                        "customer_id",
                                        order_to_update,
                                    )
                                else:
                                    continue

                        break
                    
        elif orders_menu_input == 5:
            orders_list = fetch_orders()
            if len(orders_list) == 0:
                input("There is nothing to delete\nPress Enter to return")
            else:
                for order in orders_list:
                    print(
                        f"Order ID: {order['order_id']}\n"
                        f"Customer Name: {order['customer_name']}\n"
                        f"Customer Address: {order['customer_address']}\n"
                        f"Customer Phone: {order['customer_phone']}\n"
                        f"Courier: {order['courier']}\n"
                        f"Status: {order['status']}\n"
                        f"Items: {order['items']}\n"
                        f"-----------------------------"
                    )
                while True:
                    # GET user input for order index value
                    order_to_delete = get_number_input(
                        "Chose order to delete or press Enter to return to Orders Menu",
                        "number",
                        None,
                        True,
                    )

                    if order_to_delete == "":
                        break
                    else:
                        indexes = [order["order_id"] for order in orders_list]
                        if order_to_delete not in indexes:
                            print("Order id not available")
                            continue
                        else:
                            #   DELETE order at index in order list
                            delete_order_and_records(order_to_delete)
                            break
