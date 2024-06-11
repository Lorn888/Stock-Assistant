from helper_functions import get_number_input, clear_screen, print_orders_menu,order_status,group_by_key_value
from db_operation import fetch_products, fetch_couriers, fetch_orders, fetch_statuses, create_order, update_table_value


def orders_menu(orders_list, order_status, couriers_list, products_list):

    def status_list_with_index():
        for status in order_status:
            print(f"{order_status.index(status)}-{status}")
    def couriers_list_with_index():
        for courier in couriers_list:
            print(f"{couriers_list.index(courier)}-{courier}")
    def orders_list_with_index():
        for order in orders_list:
            print(f"{orders_list.index(order)}-{order}")
    
    while True:
        clear_screen()
        # Print orders menu options
        print_orders_menu()
        # GET user input for orders menu option
        orders_menu_input = get_number_input("Please enter your choice (0-5): ","number",5,True)
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
                for orders in orders_list:
                    print(orders)
                    print("-----------")
                # for order in orders_list:
                #     print(order)
                input("Press enter to return to the Orders Menu")

        elif orders_menu_input == 2:
    # GET user input for customer name
            print("===================================")
            customer_name_input = input("Insert Customer name or press Enter to return to Orders Menu")
            if customer_name_input:
                customer_adress_input = input("Insert Customer address or press Enter to cancel and return to the Orders Menu")
                if customer_adress_input:
                    customer_phone_input = get_number_input("Insert Customer phone number or press Enter to cancel and return to Orders Menu", "phone", None, True)
                    if customer_phone_input:
                        products_list = fetch_products()
                        for product in products_list:
                            print(f"{product['product_id']}: {product['name']} - £{product['price']}")
                        # GET user inputs for comma-separated list of product index values
                        prod_index_val_input = input(
                            "type comma-separated list (no spaces) of product index values or press Enter to cancel and return to Orders Menu")
                        
                        index_list = prod_index_val_input.strip(",").split(",")
                        index_list = [int(num) for num in index_list]  # Filter out empty strings
                        if index_list:
                            couriers_list = fetch_couriers()
                            for courier in couriers_list:
                                print(f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}")
                            while True:
                                # GET user input for courier index to select courier
                                select_courier_input = get_number_input("Select a courier","number", None, True)
                                if select_courier_input == "":
                                    break
                                select_courier_input = int(select_courier_input)
                                indexes = [courier['courier_id'] for courier in couriers_list]
                                if select_courier_input not in indexes:
                                    print("Courier with this id is not available")
                                    continue
                                else:
                                    create_order(customer_name_input,customer_adress_input,customer_phone_input,select_courier_input,1,prod_index_val_input)
                                    break  # Exit the courier selection loop
                        else:
                            print("No product index values provided. Returning to Orders Menu.")
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
                    print(f"Order ID: {order['order_id']}\n"
                    f"Customer Name: {order['customer_name']}\n"
                    f"Customer Address: {order['customer_address']}\n"
                    f"Customer Phone: {order['customer_phone']}\n"
                    f"Courier: {order['courier']}\n"
                    f"Status: {order['status']}\n"
                    f"Items: {order['items']}\n"
                    f"-----------------------------")


                # GET user input for order index value
                order_status_to_update_input = get_number_input("Chose the order to update the status of of press Enter to return to Orders Menu","number",None,True)
                if order_status_to_update_input != "":
                    # PRINT order status list with index values
                    statuses_list = fetch_statuses()
                    for status in statuses_list:
                        print(f"{status['status_id']}: {status['order_status']}")
                    
                    # GET user input for order status index value
                    updated_status_input = get_number_input("What would you like to update it to? Or press Enter to cancel changes","number",None, True)
                    if updated_status_input != "":

                    # UPDATE status for order
                        update_table_value('orders','status',updated_status_input,'order_id',order_status_to_update_input)
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
                        print(f"Order ID: {order['order_id']}\n"
                        f"Customer Name: {order['customer_name']}\n"
                        f"Customer Address: {order['customer_address']}\n"
                        f"Customer Phone: {order['customer_phone']}\n"
                        f"Courier: {order['courier']}\n"
                        f"Status: {order['status']}\n"
                        f"Items: {order['items']}\n"
                        f"-----------------------------")
                while True:
                    order_to_update = get_number_input("Chose order to update or press Enter to return to Orders Menu: ","number", None, True)
                    if order_to_update == "":
                        break
                    
                    indexes = [order['order_id'] for order in orders_list]
                    
                    if order_to_update not in indexes:
                        print("That order id is not available")
                        continue
                    # FOR EACH key-value pair in selected order:
                    else:
                        for i in orders_list[0]:
                            if i == "order_id":
                                continue

                            elif i == "courier":
                                for courier in couriers_list:
                                    print("-----------")
                                    print(f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}")
                                update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ", "number", None, True)
                                if update_input != "":
                                    update_table_value('orders','courier', update_input , 'order_id', order_to_update )
                                else:
                                    continue                                    
                            elif i == "status":
                                statuses_list = fetch_statuses()
                                for status in statuses_list:
                                    print("-----------")
                                    print(f"{status['status_id']}: {status['order_status']}")
                                update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ","number", None, True)
                                if update_input != "":
                                    update_table_value('orders','status',update_input,'order_id',order_to_update)
                                else:
                                    continue
                            elif i == "customer_phone":
                                update_input = get_number_input(f"Type new {i}\nOr press Enter to skip: ","phone",None,True)
                                if update_input != "":
                                    update_table_value('orders','customer_phone',update_input,'order_id',order_to_update)
                                else:
                                    continue
                            # GET user input for updated property
                            else:    
                                update_input = input(f"Type new {i}\nOr press Enter to skip: ")
                                if len(update_input) == 0:
                                    continue
                                else:
                                    update_table_value('orders',i,update_input,'order_id',order_to_update)
                            # do not update this property
                            
                    
                        break
        elif orders_menu_input == 5:
            if len(orders_list) == 0:
                input("There is nothing to delete\nPress Enter to return")
            else:
            # PRINT orders list
                orders_list_with_index()
                # GET user input for order index value
                order_to_delete = get_number_input("Chose order to delete or press Enter to return to Orders Menu",(len(orders_list)-1))
                if order_to_delete != "":
                #   DELETE order at index in order list
                    del orders_list[order_to_delete]
                else:
                    continue