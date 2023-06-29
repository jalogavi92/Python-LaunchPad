# Create an empty phone book dictionary
phone_book = {}

def add_contact(name, number):
    phone_book[name] = number
    print(f"Contact {name} added with phone number {number}.")

def search_contact(name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Contact '{name}' does not exist in the phone book.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' does not exist in the phone book.")

def display_contacts():
    if phone_book:
        print("Phone Book:")
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Phone Book is empty.")

def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == "3":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Exiting Phone Book.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
