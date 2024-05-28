import csv

# LOAD products list from products.csv
products_list =[]
try:
    with open("week4//data//products.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        products_list = [row for row in reader]
except Exception as e:
    print(e)


# LOAD couriers list from couriers.csv
couriers_list =[]
try:
    with open("week4//data//couriers.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        couriers_list = [row for row in reader]
except Exception as e:
    print(e)

# LOAD orders from orders.csv
orders_list =[]
try:
    with open("week4//data//orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        orders_list = [row for row in reader]
except Exception as e:
    print(e)

print(orders_list)
print(couriers_list)
print(products_list)


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
        # SAVE products list to products.txt
        try:
            with open("week3/data/products.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(products_list)
        except Exception as e:
            print(e)
        # SAVE couriers list to couriers.txt
        try:
            with open("week3/data/couriers.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(couriers_list)
        except Exception as e:
            print(e)

        break

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
                # APPEND product name to products list
                products_list.append(new_product_input)

            elif product_menu_input == 3:

                for product in products_list:
                    # PRINT product names with its index value
                    print(f"{products_list.index(product)}-{product}")
                # GET user input for product index value
                product_to_update_input = int(input("Chose the product to update"))
                # GET user input for new product name
                new_product_name = input("Type the name of the new product")
                # UPDATE product name at index in products list
                products_list[product_to_update_input] = new_product_name
                print(products_list)

            elif product_menu_input == 4:
                # PRINT products list
                for product in products_list:
                    print(f"{products_list.index(product)}-{product}")
                # GET user input for product index value
                product_to_delete = int(input("Chose the product to delete"))
                # DELETE product at index in products list
                products_list.remove(products_list[product_to_delete])
                print(products_list)
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
                new_courier_input = input("Type new couriers nema:")
                # APPEND courier name to couriers list
                couriers_list.append(new_courier_input)
            elif courier_menu_input == 3:
                for courier in couriers_list:
                    # PRINT courier names with its index value
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                update_courier_input = int(input("Chose courier to update"))
                # GET user input for new courier name
                new_courier_input = input("Type new couriers name")
                # UPDATE courier name at index in couriers list
                couriers_list[update_courier_input] = new_courier_input
            elif courier_menu_input == 4:
                # PRINT courier list
                for courier in couriers_list:
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                delete_courier_input = int(input("Chose courier to delete"))
                # DELETE courier at index in courier list
                couriers_list.remove(couriers_list[delete_courier_input])

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
                customer_name_input = input("Insert Customer name eg.'Harry Potter'")
                # name_list = customer_name_input.split(" ")
                # print(name_list)
                # GET user input for customer address
                customer_adress_input = input(
                    "Insert Customer adress eg.'Unit 2, 12 Main Street, LONDON, WH1 2ER'"
                )
                # GET user input for customer phone number
                customer_phone_input = input(
                    "Insert Customer phone number eg.'0789887334'"
                )
                # PRINT couriers list with index value for each courier
                for courier in couriers_list:
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index to select courier
                select_courier_input = int(input("Select a courier"))

                customer_order = {
                    "name": customer_name_input,
                    "address": customer_adress_input,
                    "phone": customer_phone_input,
                    "order_status": order_status[0],
                    "courier": couriers_list[select_courier_input],
                }
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
                orders_list[order_status_to_update_input]["order_status"] = (
                    order_status[updated_status_input]
                )

            elif orders_menu_input == 4:
                # PRINT orders list with its index values
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_update = int(input("Chose order to update"))
                # FOR EACH key-value pair in selected order:
                for i in orders_list[order_to_update]:
                    # GET user input for updated property
                    update_input = input(i)
                    # update the property value with user input
                    if len(update_input) > 0:
                        orders_list[order_to_update][i] = update_input
                    else:
                        # do not update this property
                        orders_list[order_to_update][i] = orders_list[order_to_update][
                            i
                        ]

            elif orders_menu_input == 5:
                # PRINT orders list
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                # GET user input for order index value
                order_to_delete = int(input("Chose order to delete"))
                #   DELETE order at index in order list
                del orders_list[order_to_delete]
