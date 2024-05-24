import csv

# LOAD products list from products.txt
try:
    with open("week3//data//products.csv", "r") as file:
        reader = csv.reader(file)
        for products_list in reader:
            print(products_list)
except Exception as e:
    print(e)

# LOAD couriers list from couriers.txt
try:
    with open("week3//data//couriers.csv", "r") as file:
        reader = csv.reader(file)
        for couriers_list in reader:
            print(couriers_list)
except Exception as e:
    print(e)

# CREATE orders list of dictionaries
orders_list = [
    {
        "name": "Harry Potter",
        "address": "Unit 2, 12 Main Street, London",
        "phone": "07954433211"
    },
    {
        "name": "Hermione Granger",
        "address": "Apartment 4, 7 Baker Street, London",
        "phone": "07891234567"
    },
    {
        "name": "Ron Weasley",
        "address": "Cottage 1, Ottery St Catchpole, Devon",
        "phone": "07781234567"
    },
    {
        "name": "Albus Dumbledore",
        "address": "The Headmaster's Office, Hogwarts School of Witchcraft and Wizardry",
        "phone": "07651234567"
    },
    {
        "name": "Rubeus Hagrid",
        "address": "Hagrid's Hut, Hogwarts School of Witchcraft and Wizardry",
        "phone": "07551234567"
    }
]

# CREATE order status list
order_status = ["PREPARING","READY","SHIPPED"] 

main_menu_options = ["0-Exit App", 
    "1-Product Menu",
    "2-Couriers Menu", 
    "3-Orders Menu"]

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

order_menu_options = [
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
        print(courier_menu_options)
    
    elif main_menu_input == 3:
        
        while True:

            print(orders_menu_options)
            orders_menu_input = int(input("Chose from above Orders Menu"))

            if orders_menu_input == 0:
                break

            elif orders_menu_input == 1:
                print(orders_list)

            elif orders_menu_input == 2:
                customer_name_input = input("Insert Customer name eg.'Harry Potter'")
                # name_list = customer_name_input.split(" ")
                # print(name_list)
                customer_adress_input = input(
                    "Insert Customer adress eg.'Unit 2, 12 Main Street, LONDON, WH1 2ER'"
                )
                customer_phone_input = input(
                    "Insert Customer phone number eg.'0789887334'"
                )
                # last_dig = (customer_phone_input[-4:])
                # print([last_dig])
                order_status = "PREPARING"
                # customer_order_id = f"{name_list[0]}-{name_list[1]}-{last_dig}"
                # orders_list.append

                customer_order = {
                    "name": customer_name_input,
                    "address": customer_adress_input,
                    "phone": customer_phone_input,
                    "order_status": order_status,
                }
                orders_list.append(customer_order)
                


            elif orders_menu_input == 3:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_status_to_update_input = int(
                    input("Chose the order to update the status")
                )
                print(
                    f"{order_status_to_update_input}-{orders_list[order_status_to_update_input]['order_status']}"
                )
                updated_status_input = input("What would you like to update it to?")
                orders_list[order_status_to_update_input][
                    "order_status"
                ] = updated_status_input

            elif orders_menu_input == 4:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_to_update = int(input("Chose order to update"))

                name_update_input = input("name:")
                if len(name_update_input) > 0:
                    orders_list[order_to_update]["name"] = name_update_input

                adress_update_input = input("address:")
                if len(adress_update_input) > 0:
                    orders_list[order_to_update]["address"] = adress_update_input

                phone_update_input = input("phone:")
                if len(phone_update_input) > 0:
                    orders_list[order_to_update]["phone"] = phone_update_input

            elif orders_menu_input == 5:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_to_delete = int(input("Chose order to delete"))
                del orders_list[order_to_delete]
