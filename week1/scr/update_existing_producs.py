while True:  # Outer loop
    print("Outer loop")
    while True:  # Inner loop
        print("Inner loop")
        user_input = input("Enter 'quit' to exit inner loop, 'back' to return to outer loop: ")
        if user_input == 'quit':
            break  # Exit inner loop
        elif user_input == 'back':
            break  # Exit inner loop to return to outer loop
    if user_input == 'quit':
        print("Exiting the program...")
        break  # Exit outer loop