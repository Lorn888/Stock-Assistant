from helper_functions import *
from db_functions import *

def couriers_menu():
    while True:
        clear_screen()
        print_couriers_menu()
        courier_menu_input = get_number_input(
            "Please enter your choice (0-4): ", "number", 4, True
        )
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
            new_courier_input = input(
                "Type new couriers name or press Enter to return to Couriers Menu: "
            )
            if new_courier_input:
                print("===================================")
                new_courier_number = get_number_input(
                    "Type new couriers phone number or press Enter to cancel and return to Couriers Menu:",
                    "phone",
                    None,
                    True,
                )
                if new_courier_number is not "":
                    create_courier(new_courier_input, new_courier_number)
                else:
                    continue
            else:
                continue
        # Update Existing courier
        elif courier_menu_input == 3:
            couriers_list = fetch_couriers()
            if len(couriers_list) == 0:
                input("there is nothing to update!\nPress Enter to return")
            else:
                for courier in couriers_list:
                    print("-----------")
                    print(
                        f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}"
                    )
                print("===================================")

                while True:
                    update_courier_input = get_number_input(
                        "Chose courier to update or press Enter to return to Couriers Menu: ",
                        "number",
                        None,
                        True,
                    )
                    if update_courier_input == "":
                        break

                    update_courier_input = int(update_courier_input)
                    indexes = [courier["courier_id"] for courier in couriers_list]

                    if update_courier_input not in indexes:
                        print("That courier is not available")
                        continue
                    else:
                        for courier in couriers_list:
                            if courier["courier_id"] == update_courier_input:
                                for key in courier:
                                    if key == "courier_id":
                                        continue
                                    else:
                                        print("===================================")
                                        user_input = input(
                                            f"Type new {key}\nOr press Enter to skip: "
                                        )
                                        if len(user_input) <= 0:
                                            continue
                                        elif key == "phone":
                                            while True:
                                                if user_input == "":
                                                    break
                                                try:
                                                    update_courier_phone(
                                                        update_courier_input, user_input
                                                    )
                                                    break
                                                except ValueError:
                                                    print(
                                                        "Error: Please enter a valid phone number(use only numbers)."
                                                    )
                                                user_input = input(
                                                    "Please enter a valid number or press Enter to skip: "
                                                )
                                        else:
                                            update_courier_name(
                                                update_courier_input, user_input
                                            )
                        break
        # Delete Courier
        elif courier_menu_input == 4:

            couriers_list = fetch_couriers()
            if len(couriers_list) == 0:
                input("There is nothing to delete!\nPress Enter to return")
            else:
                for courier in couriers_list:
                    print("-----------")
                    print(
                        f"{courier['courier_id']}: {courier['name']} - phone number:{courier['phone']}"
                    )
                print("===================================")

                while True:
                    courier_to_delete = get_number_input(
                        "Choose the product to delete or press Enter to go back to Products Menu: ",
                        "number",
                        None,
                        True,
                    )
                    if courier_to_delete == "":
                        break

                    courier_to_delete = int(courier_to_delete)
                    indexes = [courier["courier_id"] for courier in couriers_list]

                    if courier_to_delete not in indexes:
                        print("Courier with this id is not available")
                        continue
                    else:
                        delete_courier(courier_to_delete)
                        print(f"Product with ID {courier_to_delete} has been deleted.")
                        break
