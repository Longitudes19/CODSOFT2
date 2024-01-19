class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

     def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print(f"Contact {old_name} updated successfully.")
                return
        print(f"No contact found with the name {old_name}.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"No contact found with the name {name}.")

# Sample usage:
contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        new_contact = Contact(name, phone_number, email, address)
        contact_book.add_contact(new_contact)

    elif choice == "2":
        contact_book.view_contact_list()

    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        contact_book.search_contact(query)

    elif choice == "4":
        old_name = input("Enter the name of the contact to update: ")
        name = input("Enter New Name: ")
        phone_number = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")
        address = input("Enter New Address: ")
        new_contact = Contact(name, phone_number, email, address)
        contact_book.update_contact(old_name, new_contact)

    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        contact_book.delete_contact(name)

    elif choice == "0":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
