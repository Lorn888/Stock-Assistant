def couriers_menu(couriers_list):
    courier_menu_options = [
    "0-Return to the Main Menu",
    "1-Print courier list",
    "2-Create a new Courier",
    "3-Update Existing Courier",
    "4-Delete Order",
]
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