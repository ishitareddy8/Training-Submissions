import random
import string

# 1️⃣ UNDERSTAND THE PROBLEM
# → We need to generate a random password based on user preferences.

# 2️⃣ BREAK INTO SMALLER PARTS
# We'll make separate functions for:
# - getting user input
# - building the character pool
# - generating the password
# - displaying the result

# Step 1: Getting user preferences
def get_user_preferences():
    print("Welcome to the Password Generator!")
    length = int(input("Enter password length: "))
    include_uppercase = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    include_digits = input("Include digits? (Y/N): ").lower() == 'y'
    include_symbols = input("Include symbols? (Y/N): ").lower() == 'y'
    
    return length, include_uppercase, include_digits, include_symbols


# Step 2: Build character pool 
def build_character_pool(include_uppercase, include_digits, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return characters


# Step 3: Generate password 
def generate_password(length, characters):
    # Optional improvement: ensure at least one of each type (if selected)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Step 4: Display result 
def display_password(password):
    print("\n Your generated password is:", password)


# Step 5: Combine everything (Main function)
def main():
    # Get inputs
    length, upper, digits, symbols = get_user_preferences()

    # Build the pool
    char_pool = build_character_pool(upper, digits, symbols)

    # Generate password
    password = generate_password(length, char_pool)

    # Display it
    display_password(password)


# Run the program
if __name__ == "__main__":
    main()
