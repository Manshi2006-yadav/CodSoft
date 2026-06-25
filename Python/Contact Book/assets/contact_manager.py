from assets.file_handler import load_contacts, save_contacts


def add_contact(name, phone, email, address):
    contacts = load_contacts()

    for contact in contacts:
        if contact["phone"] == phone:
            return False

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    return True


def view_contacts():
    return load_contacts()


def search_contact(keyword):
    contacts = load_contacts()

    results = []

    for contact in contacts:
        if (
            keyword.lower() in contact["name"].lower()
            or keyword in contact["phone"]
        ):
            results.append(contact)

    return results


def delete_contact(phone):
    contacts = load_contacts()

    updated_contacts = []

    found = False

    for contact in contacts:
        if contact["phone"] != phone:
            updated_contacts.append(contact)
        else:
            found = True

    save_contacts(updated_contacts)

    return found


def update_contact(phone, new_name, new_email, new_address):
    contacts = load_contacts()

    found = False

    for contact in contacts:

        if contact["phone"] == phone:
            contact["name"] = new_name
            contact["email"] = new_email
            contact["address"] = new_address
            found = True

    save_contacts(contacts)

    return found