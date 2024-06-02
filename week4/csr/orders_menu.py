from helper_functions import get_number_input, clear_screen, print_orders_menu

def orders_menu(orders_list, order_status, couriers_list, products_list):

 

    while True:
        clear_screen()
        # Print orders menu options
        print_orders_menu()
        # GET user input for orders menu option
        orders_menu_input = get_number_input("Please enter your choice (0-5): ")
        clear_screen()
        if orders_menu_input == 0:
            #  RETURN to main menu
            break

        elif orders_menu_input == 1:
            # PRINT orders dictionary
            if len(orders_list) == 0:
                input("Orders list is empty\nPress Enter to return")
            else:
                for order in orders_list:
                    print(order)
                    print("-----------")
                input("Press enter to return to the Orders Menu")

        elif orders_menu_input == 2:
            # GET user input for customer name
            print("===================================")
            customer_name_input = input("Insert Customer name or press Enter to return to Orders Menu")
            if customer_name_input:
                # name_list = customer_name_input.split(" ")
                # print(name_list)
                # GET user input for customer address
                customer_adress_input = input(
                    "Insert Customer adress or press Enter to cancel and return to the Orders Menu")
                if customer_adress_input:
                # GET user input for customer phone number
                    customer_phone_input = get_number_input("Insert Customer phone number or press Enter to cancel and return to Orders Menu")
                    if customer_phone_input:
                    # PRINT products list with its index values
                        for product in products_list:
                            print(f"{products_list.index(product)}-{product}")
                        # GET user inputs for comma-separated list of product index values
                        prod_index_val_input = input(
                            "type comma-separated list of product index values or press Enter to cancel and return to Orders Menu")
                        if prod_index_val_input:

                            # PRINT couriers list with index value for each courier
                            for courier in couriers_list:
                                print(f"{couriers_list.index(courier)}-{courier}")
                            # GET user input for courier index to select courier
                            select_courier_input = get_number_input("Select a courier")
                            if select_courier_input is not "":


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
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

        elif orders_menu_input == 3:
            # PRINT orders list with its index values
            if len(orders_list) == 0:
                input("There is no orders in the list\nPress Enter to return")
            else:
                orders_list_with_index()
                # GET user input for order index value
                order_status_to_update_input = get_number_input("Chose the order to update the status of of press Enter to return to Orders Menu")
                if order_status_to_update_input is not "":
                    # PRINT order status list with index values
                
                    status_list_with_index()
                    # GET user input for order status index value
                    updated_status_input = get_number_input("What would you like to update it to? Or press Enter to cancel changes")
                    if updated_status_input is not "":

                    # UPDATE status for order
                        orders_list[order_status_to_update_input]["status"] = order_status[
                            updated_status_input]
                    else:
                        continue
                else:
                    continue

        elif orders_menu_input == 4:
            # PRINT orders list with its index values
            if len(orders_list) == 0:
                input("there is nothing to update\nPress Enter to return")
            else:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_update = get_number_input("Chose order to update or press Enter to return to Orders Menu: ")
                if order_to_update is not "":
                # FOR EACH key-value pair in selected order:
                    for i in orders_list[order_to_update]:
                        if i == "courier":
                            couriers_list_with_index()
                            update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ")
                            if update_input is not "":
                                orders_list[order_to_update][i] = update_input
                            else:
                                continue                                    
                        elif i == "status":
                            status_list_with_index()
                            update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ")
                            if update_input is not "":
                                orders_list[order_to_update][i] = update_input
                            else:
                                continue
                        elif i == "customer phone":
                            update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ")
                            if update_input is not "":
                                orders_list[order_to_update][i] = update_input
                            else:
                                continue
                        # GET user input for updated property
                        else:    
                            update_input = input(f"Type new {i}\nOr press Enter to skip: ")
                            if len(update_input) == 0:
                                continue
                            else:
                                orders_list[order_to_update][i] = update_input
                        # do not update this property
                        
                else:
                    continue
        elif orders_menu_input == 5:
            if len(orders_list) == 0:
                input("There is nothing to delete\nPress Enter to return")
            else:
            # PRINT orders list
                orders_list_with_index()
                # GET user input for order index value
                order_to_delete = get_number_input("Chose order to delete or press Enter to return to Orders Menu")
                if order_to_delete is not "":
                #   DELETE order at index in order list
                    del orders_list[order_to_delete]
                else:
                    continue