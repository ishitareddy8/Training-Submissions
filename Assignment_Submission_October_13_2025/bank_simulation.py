def bank_simulation():
    print("Bank deposit & Withdrawal Simulation!")
    balance = 0.0  # starting balance

    while True:
        print("\n------ MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # Check Balance
        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")

        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount ($): "))
                if amount > 0:
                    balance += amount
                    print(f"Successfully deposited ${amount:.2f}")
                    print(f"New Balance: ${balance:.2f}")
                else:
                    print("Deposit amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount ($): "))
                if amount > balance:
                    print("Insufficient funds!")
                elif amount <= 0:
                    print("Withdrawal amount must be greater than 0.")
                else:
                    balance -= amount
                    print(f"Withdrawn ${amount:.2f}")
                    print(f"Remaining Balance: ${balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Exit
        elif choice == "4":
            print("Thank you for using Python Bank. Have a great day!")
            break

        else:
            print("Invalid option! Please choose between 1 and 4.")

# Run the program
bank_simulation()
