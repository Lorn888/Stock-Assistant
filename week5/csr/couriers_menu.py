from helper_functions import get_number_input, clear_screen, print_couriers_menu 
from db_operation import fetch_couriers, create_courier

def couriers_menu(couriers_list):
    while True:
        clear_screen()
        print_couriers_menu()
        courier_menu_input = get_number_input("Please enter your choice (0-4): ","number", 4, True)
        clear_screen()
        # Return to the main manu
        if courier_menu_input == 0:
            break
        # Couriers List        
        elif courier_menu_input == 1:
            couriers_list = fetch_couriers()
            if len(couriers_list) == 0:
                input("Couriers list is empty\nPress Enter to return")
            else:
                for courier in couriers_list:
                    print(f"{courier['name']} - phone number:{courier['phone']}")
                    print("-----------")
                input("Press enter to return to the Couriers Menu")
        # Create new courier
        elif courier_menu_input == 2:
            # GET user input for courier name
            print("===================================")
            new_courier_input = input("Type new couriers name or press Enter to return to Couriers Menu: ")
            if new_courier_input:
                print("===================================")
                new_courier_number = get_number_input("Type new couriers phone number or press Enter to cancel and return to Couriers Menu:", "phone", None, True)
                if new_courier_number is not "":
                    create_courier(new_courier_input, new_courier_number)
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
                update_courier_input = get_number_input("Chose courier to update or press Enter to return to Couriers Menu: ",(len(couriers_list)-1))
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
                delete_courier_input = get_number_input("Chose courier to delete or press Enter to go back to Couriers Menu: ", (len(couriers_list)-1))
                if delete_courier_input is not "":
                        # DELETE courier at index in courier list
                    couriers_list.remove(couriers_list[delete_courier_input])
                else:
                    continue