import csv

# LOAD products list from products.csv
try:
    with open("week4//data//products.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        products_list = [row for row in reader]
except Exception as e:
    print(e)


# LOAD couriers list from couriers.csv
couriers_list = []
try:
    with open("week4//data//couriers.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        couriers_list = [row for row in reader]
except Exception as e:
    print(e)

# LOAD orders from orders.csv
orders_list = []
try:
    with open("week4//data//orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        orders_list = [row for row in reader]
except Exception as e:
    print(e)

# print(orders_list)
# print(couriers_list)
# print(products_list)


# CREATE order status list
order_status = ["PREPARING", "READY", "SHIPPED"]

main_menu_options = ["0-Exit App", "1-Product Menu", "2-Couriers Menu", "3-Orders Menu"]

product_menu_options = [
    "0-Return to the Main Menu",
    "1-Products List",
    "2-Create New Product",
    "3-Update EXisting Product",
    "4-Delete Product",
]

courier_menu_options = [
    "0-Return to the Main Menu",
    "1-Print courier list",
    "2-Create a new Courier",
    "3-Update Existing Courier",
    "4-Delete Order",
]

orders_menu_options = [
    "0-Return to the Main Menu",
    "1-Print orders dictionary",
    "2-Create a new order",
    "3-Update Existing Order Status",
    "4-Update Existing Order",
    "5-Delete Order",
]


while True:
    # PRINT main menu options
    print(main_menu_options)
    # GET user input for main menu option
    main_menu_input = int(input("Chose from the above 3 options '0-3'"))

    if main_menu_input == 0:
        # SAVE products list to products.csv
        try:
            header = ["name", "price"]
            with open("week4/data/products.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for row in products_list:
                    writer.writerow(row)
        except Exception as e:
            print(e)
        # SAVE couriers list to couriers.txt
        try:
            header = ["name", "phone"]
            with open("week4/data/couriers.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for row in couriers_list:
                    writer.writerow(row)
        except Exception as e:
            print(e)
        # SAVE orders list to order.csv
        try:
            header = [
                "customer_name",
                "customer_address",
                "customer_phone",
                "courier",
                "status",
                "items",
            ]
            with open("week4/data/orders.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for row in orders_list:
                    writer.writerow(row)
        except Exception as e:
            print(e)
        # EXIT app
        break

    # Product Menu
    elif main_menu_input == 1:
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

    # Couriers Menu
    elif main_menu_input == 2:
        while True:
            # PRINT courier menu options
            print(courier_menu_options)
            # GET user input for courier menu option
            courier_menu_input = int(input("Chose from above courier menu"))
            if courier_menu_input == 0:
                # RETURN to main menu
                break
            elif courier_menu_input == 1:
                # PRINT couriers list
                print(couriers_list)
            elif courier_menu_input == 2:
                # GET user input for courier name
                new_courier_input = input("Type new couriers name:")
                # GET user input for courier phone number
                new_courier_number = input("Type new couriers number:")
                # CREATE new courier dictionary with above properties
                new_courier = {"name": new_courier_input, "phone": new_courier_number}
                # APPEND courier dictionary to courier list
                couriers_list.append(new_courier)
            elif courier_menu_input == 3:
                for courier in couriers_list:
                    # PRINT courier names with its index value
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                update_courier_input = int(input("Chose courier to update"))
                # GET user input for new courier name

                for i in couriers_list[update_courier_input]:
                    # GET user input for updated property
                    user_input = input(i)
                    if len(user_input) <= 0:
                        # do not update this property and skip
                        couriers_list[update_courier_input][i] = [i]
                    else:
                        # update the property value with user input
                        couriers_list[update_courier_input][i] = user_input
            elif courier_menu_input == 4:
                # PRINT courier list
                for courier in couriers_list:
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                delete_courier_input = int(input("Chose courier to delete"))
                # DELETE courier at index in courier list
                couriers_list.remove(couriers_list[delete_courier_input])

    # Orders Menu
    elif main_menu_input == 3:
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
                    # update the property value with user input
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
                        # do not update this property
                        orders_list[order_to_update][i] = update_input

            elif orders_menu_input == 5:
                # PRINT orders list
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_delete = int(input("Chose order to delete"))
                #   DELETE order at index in order list
                del orders_list[order_to_delete]
