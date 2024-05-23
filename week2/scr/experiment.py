import json
product_list = ["coke-zero", "corona", "water", "sprite"]
orders_list = [
    # Test lists
    # {
    #     "name": "Harry Potter",
    #     "address": "Unit 2, 12 Main Street, London",
    #     "phone": "07954433211",
    #     "order_status": "PREPARING",
    # },
    # {
    #     "name": "Hermione Granger",
    #     "address": "Apartment 4, 7 Baker Street, London",
    #     "phone": "07891234567",
    #     "order_status": "PREPARING",
    # },
    # {
    #     "name": "Ron Weasley",
    #     "address": "Cottage 1, Ottery St Catchpole, Devon",
    #     "phone": "07781234567",
    #     "order_status": "PREPARING",
    # },
    # {
    #     "name": "Albus Dumbledore",
    #     "address": "The Headmaster's Office, Hogwarts School of Witchcraft and Wizardry",
    #     "phone": "07651234567",
    #     "order_status": "PREPARING",
    # },
    # {
    #     "name": "Rubeus Hagrid",
    #     "address": "Hagrid's Hut, Hogwarts School of Witchcraft and Wizardry",
    #     "phone": "07551234567",
    #     "order_status": "PREPARING",
    # },
]

main_menu_options = ["0-Exit App", "1-Product Menu", "2-Orders Menu"]

product_menu_options = [
    "0-Return to the Main Menu",
    "1-Products List",
    "2-Create New Product",
    "3-Update Existing Product",
    "4-Delete Product",
]

orders_menu_options = [
    "0-Return to the Main Menu",
    "1-Print orders dictionary",
    "2-Create a new order",
    "3-Update Existing Order Status",
    "4-Update Existing Order",
    "5-Delete Order",
]

print(main_menu_options)

try:
    orders_file = open("week2//data//orders_file.json", "r+")
    orders_list = json.load(orders_file)
    orders_file.close()

except Exception as e:
    print(e)
finally:
    print("file closed")


while True:
    main_menu_input = int(input("Choose from the above 3 options '0-2'"))

    if main_menu_input == 0:
        break

    elif main_menu_input == 1:
        while True:
            print(product_menu_options)
            product_menu_input = int(input("Choose from above product menu"))

            if product_menu_input == 0:
                break

            elif product_menu_input == 1:
                print(product_list)

            elif product_menu_input == 2:
                new_product_input = input("Type the name of the new product")
                product_list.append(new_product_input)

            elif product_menu_input == 3:
                for product in product_list:
                    print(f"{product_list.index(product)}-{product}")
                product_to_update_input = int(input("Choose the product to update"))
                new_product_name = input("Type the name of the new product")
                product_list[product_to_update_input] = new_product_name
                print(product_list)

            elif product_menu_input == 4:
                for product in product_list:
                    print(f"{product_list.index(product)}-{product}")
                product_to_delete = int(input("Choose the product to delete"))
                product_list.remove(product_list[product_to_delete])
                print(product_list)

    elif main_menu_input == 2:
        while True:
            print(orders_menu_options)
            orders_menu_input = int(input("Choose from above Orders Menu"))

            if orders_menu_input == 0:
                break

            elif orders_menu_input == 1:
                print(orders_list)

            elif orders_menu_input == 2:
                customer_name_input = input("Insert Customer name eg.'Harry Potter'")
                customer_address_input = input(
                    "Insert Customer address eg.'Unit 2, 12 Main Street, LONDON, WH1 2ER'"
                )
                customer_phone_input = input(
                    "Insert Customer phone number eg.'0789887334'"
                )
                order_status = "PREPARING"

                customer_order = {
                    "name": customer_name_input,
                    "address": customer_address_input,
                    "phone": customer_phone_input,
                    "order_status": order_status,
                }
                orders_list.append(customer_order)

                # Open the file in write mode and dump the updated orders_list
                try:
                    orders_file = open("week2//data//orders_file.json", "w")
                    json.dump(orders_list, orders_file)
                    orders_file.close()
                except Exception as e:
                    print(e)

            elif orders_menu_input == 3:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_status_to_update_input = int(
                    input("Choose the order to update the status")
                )
                print(
                    f"{order_status_to_update_input}-{orders_list[order_status_to_update_input]['order_status']}"
                )
                updated_status_input = input("What would you like to update it to?")
                orders_list[order_status_to_update_input][
                    "order_status"
                ] = updated_status_input

                # Open the file in write mode and dump the updated orders_list
                try:
                    orders_file = open("week2//data//orders_file.json", "w")
                    json.dump(orders_list, orders_file)
                    orders_file.close()
                except Exception as e:
                    print(e)

            elif orders_menu_input == 4:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_to_update = int(input("Choose order to update"))

                name_update_input = input("name:")
                if len(name_update_input) > 0:
                    orders_list[order_to_update]["name"] = name_update_input

                address_update_input = input("address:")
                if len(address_update_input) > 0:
                    orders_list[order_to_update]["address"] = address_update_input

                phone_update_input = input("phone:")
                if len(phone_update_input) > 0:
                    orders_list[order_to_update]["phone"] = phone_update_input

                # Open the file in write mode and dump the updated orders_list
                try:
                    orders_file = open("week2//data//orders_file.json", "w")
                    json.dump(orders_list, orders_file)
                    orders_file.close()
                except Exception as e:
                    print(e)

            elif orders_menu_input == 5:
                for order in orders_list:
                    print(f"{orders_list.index(order)}-{order}")
                order_to_delete = int(input("Choose order to delete"))
                del orders_list[order_to_delete]

                # Open the file in write mode and dump the updated orders_list
                try:
                    orders_file = open("week2//data//orders_file.json", "w")
                    json.dump(orders_list, orders_file)
                    orders_file.close()
                except Exception as e:
                    print(e)

print("Program exited")
