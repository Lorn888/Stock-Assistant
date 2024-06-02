from helper_functions import get_number_input, clear_screen, print_couriers_menu 

def couriers_menu(couriers_list):
    while True:
        clear_screen()
        # PRINT courier menu options
        print_couriers_menu()
        # GET user input for courier menu option
        courier_menu_input = get_number_input("Please enter your choice (0-4): ")
        clear_screen()
        if courier_menu_input == 0:
            # RETURN to main menu
            break

        elif courier_menu_input == 1:
            # PRINT couriers list
            if len(couriers_list) == 0:
                input("Couriers list is empty\nPress Enter to return")
            else:
                for courier in couriers_list:
                    print(courier)
                    print("-----------")
                input("Press enter to return to the Couriers Menu")

        elif courier_menu_input == 2:
            # GET user input for courier name
            print("===================================")
            new_courier_input = input("Type new couriers name or press Enter to return to Couriers Menu: ")
            if new_courier_input:
                print("===================================")
                new_courier_number = get_number_input("Type new couriers phone number or press Enter to cancel and return to Couriers Menu:")
                if new_courier_number is not "":
                    new_courier = {
                    "name": new_courier_input,
                    "phone": new_courier_number
            }
            # APPEND courier dictionary to courier list
                    couriers_list.append(new_courier)
                else:
                    continue
            else:
                continue

        elif courier_menu_input == 3:
            if len(couriers_list) == 0:
                input("there is nothing to update!\nPress Enter to return")
            else:
                for courier in couriers_list:
                    # PRINT courier names with its index value
                    print("-----------")
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                print("===================================")
                update_courier_input = get_number_input("Chose courier to update or press Enter to return to Couriers Menu: ")
                # GET user input for new courier name
                if update_courier_input is not "":
                    for i in couriers_list[update_courier_input]:
                        # GET user input for updated property
                        print("===================================")
                        user_input = input(f"Type new {i}\nOr press Enter to skip: ")
                        if len(user_input) <= 0:
                            # do not update this property and skip
                            continue
                        elif i == "phone":
                            while True:
                                try:
                                    number = int(user_input)
                                    couriers_list[update_courier_input][i] = number
                                    break
                                except ValueError:
                                    user_input = input("Please enter a valid number or press Enter to skip: ")
                            # update the property value with user input
                        else:
                            couriers_list[update_courier_input][i] = user_input
                else:
                    continue

        elif courier_menu_input == 4:
            # PRINT courier list
            if len(couriers_list) == 0:
                input("There is nothing to delete!\nPress Enter to return")
            else:
                for courier in couriers_list:
                    print("-----------")
                    print(f"{couriers_list.index(courier)}-{courier}")
                # GET user input for courier index value
                print("===================================")
                delete_courier_input = get_number_input("Chose courier to delete or press Enter to go back to Couriers Menu: ")
                if delete_courier_input is not "":
                        # DELETE courier at index in courier list
                    couriers_list.remove(couriers_list[delete_courier_input])
                else:
                    continue