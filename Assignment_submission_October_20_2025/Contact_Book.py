# Contact Book Program using Dictionary

# Initialize the contact book
contacts = {
    "Nayan": {"phone": "571-437-4843", "email": "nayanreddy@gmail.com"},
    "Ish": {"phone": "947-256-2056", "email": "ishhreddy@gmail.com"}
}

# Function to display all contacts
def display_contacts():
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print("-------------------")

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"{name} has been added successfully!")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"\nContact found: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted.")
    else:
        print("Contact not found.")

# Menu-driven interface
while True:
    print("\n===== Contact Book Menu =====")
    print("1. Display all contacts")
    print("2. Add a new contact")
    print("3. Search a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
