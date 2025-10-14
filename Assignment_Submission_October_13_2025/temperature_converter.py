def temperature_converter():
    print("Temperature Converter")
    print("A - Celsius to Fahrenheit")
    print("B - Fahrenheit to Celsius")
    
    choice = input("Enter your choice (A or B): ")

    if choice == "A":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

    elif choice == "B":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")

    else:
        print("Wrong choice! Please enter either A or B")

# Run the converter
temperature_converter()
