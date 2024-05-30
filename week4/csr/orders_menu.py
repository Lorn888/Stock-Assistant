def orders_menu(orders_list, order_status,couriers_list, products_list):
    orders_menu_options = [
    "0-Return to the Main Menu",
    "1-Print orders dictionary",
    "2-Create a new order",
    "3-Update Existing Order Status",
    "4-Update Existing Order",
    "5-Delete Order",
]

    while True:

            print(orders_menu_options)
            orders_menu_input = int(input("Chose from above Orders Menu"))

            if orders_menu_input == 0:
                #  RETURN to main menu
                break

            elif orders_menu_input == 1:
                # PRINT orders dictionary
                print(orders_list)

            elif orders_menu_input == 2:
                # GET user input for customer name
                customer_name_input = input("Insert Customer name")
                # name_list = customer_name_input.split(" ")
                # print(name_list)
                # GET user input for customer address
                customer_adress_input = input(
                    "Insert Customer adress eg.'Unit 2, 12 Main Street, LONDON, WH1 2ER'"
                )
                # GET user input for customer phone number
                customer_phone_input = input("Insert Customer phone number")
                # PRINT products list with its index values
                for product in products_list:
                    print(f"{products_list.index(product)}-{product}")
                # GET user inputs for comma-separated list of product index values
                prod_index_val_input = input(
                    "type comma-separated list of product index values"
                )
                # PRINT couriers list with index value for each courier
                for courier in couriers_list:
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index to select courier
                select_courier_input = int(input("Select a courier"))

                customer_order = {
                    "customer_name": customer_name_input,
                    "customer_address": customer_adress_input,
                    "customer_phone": customer_phone_input,
                    #  SET order status to be 'PREPARING'
                    "courier": select_courier_input,
                    "status": order_status[0],
                    "items": prod_index_val_input,
                }
                # APPEND order dictionary to orders list
                orders_list.append(customer_order)

            elif orders_menu_input == 3:
                # PRINT orders list with its index values
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_status_to_update_input = int(
                    input("Chose the order to update the status of")
                )
                # PRINT order status list with index values
                for status in order_status:
                    print(f"{order_status.index(status)}-{status}")
                # GET user input for order status index value
                updated_status_input = int(
                    input("What would you like to update it to?")
                )
                # UPDATE status for order
                orders_list[order_status_to_update_input]["status"] = order_status[
                    updated_status_input
                ]

            elif orders_menu_input == 4:
                # PRINT orders list with its index values
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_update = int(input("Chose order to update"))
                # FOR EACH key-value pair in selected order:
                for i in orders_list[order_to_update]:
                    if i == "courier":
                        for courier_dict in couriers_list:
                            print(f"{couriers_list.index(courier_dict)}-{courier_dict['name']}")
                    elif i == "status":
                        for status in order_status:
                            print(f"{order_status.index(status)}-{status}")
                    # GET user input for updated property
                    update_input = input(i)
                        # do not update this property
                    if len(update_input) <= 0:
                        
                        orders_list[order_to_update][i] = orders_list[order_to_update][
                            i
                        ]
                    elif i == "status":
                        if len(update_input) <= 0:
                            orders_list[order_to_update][i] = update_input
                        else:
                            orders_list[order_to_update]["status"]= order_status[int(update_input)]
                    else:
                    # update the property value with user input
                        orders_list[order_to_update][i] = update_input

            elif orders_menu_input == 5:
                # PRINT orders list
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_delete = int(input("Chose order to delete"))
                #   DELETE order at index in order list
                del orders_list[order_to_delete]
