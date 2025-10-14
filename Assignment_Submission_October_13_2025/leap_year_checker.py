def leap_year_checker():
    print("Leap Year Checker")
    
    try:
        year = int(input("Enter a year: "))
        
        # Leap year logic
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f" {year} is a leap year!")
        else:
            print(f" {year} is not a leap year.")
    
    except ValueError:
        print("Please enter a valid year.")

# Run the program
leap_year_checker()
