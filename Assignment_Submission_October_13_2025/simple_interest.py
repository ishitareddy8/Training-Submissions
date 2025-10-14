def simple_interest_calculator():
    print("Simple Interest Calculator")
    
    try:
        principal = float(input("Enter the principal amount: "))
        time = float(input("Enter the time (in years): "))
        rate = float(input("Enter the rate of interest (%): "))
        
        simple_interest = (principal * time * rate) / 100
        total_amount = principal + simple_interest

        print(f"\nPrincipal Amount: ${principal:.2f}")
        print(f"Rate of Interest: {rate:.2f}%")
        print(f"Time Period: {time:.2f} years")
        print(f"Simple Interest: ${simple_interest:.2f}")
        print(f"Total Amount after Interest: ${total_amount:.2f}")
    
    except ValueError:
        print("Please enter correct numeric values.")

# Run the program
simple_interest_calculator()
