from assets.contact_manager import *

while True:

    print("\n CONTACT BOOK ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")

        if add_contact(name, phone, email, address):
            print("Contact added successfully.")
        else:
            print("Phone number already exists.")

    elif choice == "2":

        contacts = view_contacts()

        if len(contacts) == 0:
            print("No contacts available.")

        else:
            print("\nSaved Contacts:\n")

            for index, contact in enumerate(contacts, start=1):

                print(f"Contact {index}")
                print(f"Name    : {contact['name']}")
                print(f"Phone   : {contact['phone']}")
                print(f"Email   : {contact['email']}")
                print(f"Address : {contact['address']}")
                print("-" * 30)

    elif choice == "3":

        keyword = input("Enter name or phone: ")

        results = search_contact(keyword)

        if len(results) == 0:
            print("No contact found.")

        else:
            for contact in results:

                print("\nMatch Found")
                print(f"Name    : {contact['name']}")
                print(f"Phone   : {contact['phone']}")
                print(f"Email   : {contact['email']}")
                print(f"Address : {contact['address']}")

    elif choice == "4":

        phone = input("Enter phone number of contact: ")

        new_name = input("New Name: ")
        new_email = input("New Email: ")
        new_address = input("New Address: ")

        if update_contact(
            phone,
            new_name,
            new_email,
            new_address
        ):
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":

        phone = input("Enter phone number to delete: ")

        if delete_contact(phone):
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "6":

        print("Goodbye!")
        break

    else:
        print("Invalid choice.")