import math

def calculate_area():
    print("Area Calculator")
    print("Rectangle")
    print("Circle")
    
    choice = input("Enter your choice (Rectangle or Circle): ")

    if choice == "Rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is {area:.2f} square units.")
        
    elif choice == "Circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is {area:.2f} square units.")
        
    else:
        print("Invalid choice. Please enter Rectangle or Circle.")

# Run the program
calculate_area()
