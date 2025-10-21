def unit_converter():
    print("Basic Unit Converter")
    print("Choose a conversion type:")
    print("1. Meters ↔ Kilometers")
    print("2. Grams ↔ Kilograms")
    print("3. Celsius ↔ Fahrenheit")

    choice = input("Enter your choice (1 / 2 / 3): ")

    # Meters ↔ Kilometers
    if choice == "1":
        print("\n1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        sub_choice = input("Choose direction (1 or 2): ")

        if sub_choice == "1":
            meters = float(input("Enter meters: "))
            km = meters / 1000
            print(f"{meters:.2f} meters = {km:.3f} kilometers.")
        elif sub_choice == "2":
            km = float(input("Enter kilometers: "))
            meters = km * 1000
            print(f"{km:.3f} kilometers = {meters:.2f} meters.")
        else:
            print("Invalid choice.")

    # Grams ↔ Kilograms
    elif choice == "2":
        print("\n1. Grams to Kilograms")
        print("2. Kilograms to Grams")
        sub_choice = input("Choose direction (1 or 2): ")

        if sub_choice == "1":
            grams = float(input("Enter grams: "))
            kg = grams / 1000
            print(f"{grams:.2f} grams = {kg:.3f} kilograms.")
        elif sub_choice == "2":
            kg = float(input("Enter kilograms: "))
            grams = kg * 1000
            print(f"{kg:.3f} kilograms = {grams:.2f} grams.")
        else:
            print("Invalid choice.")

    # Celsius ↔ Fahrenheit
    elif choice == "3":
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        sub_choice = input("Choose direction (1 or 2): ")

        if sub_choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
        elif sub_choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
        else:
            print("Invalid choice.")

    else:
        print("Invalid conversion type.")

# Run the program
unit_converter()