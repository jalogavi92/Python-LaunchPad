phone_book = {}

def add_entry(name, phone_number, email):
    phone_book[name] = {
        'phone_number': phone_number,
        'email': email
    }
    print("Entry added successfully.")

def remove_entry(name):
    if name in phone_book:
        del phone_book[name]
        print("Entry removed successfully.")
    else:
        print("Entry not found.")

def lookup_entry(name):
    if name in phone_book:
        entry = phone_book[name]
        print("Name:", name)
        print("Phone Number:", entry['phone_number'])
        print("Email:", entry['email'])
    else:
        print("Entry not found.")

# Example usage
add_entry("John Doe", "1234567890", "john.doe@example.com")
add_entry("Jane Smith", "9876543210", "jane.smith@example.com")

lookup_entry("John Doe")
lookup_entry("Jane Smith")
lookup_entry("Alice")
