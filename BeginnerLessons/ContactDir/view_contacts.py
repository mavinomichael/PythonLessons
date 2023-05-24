import BeginnerLessons.ContactDir.contact_manager as manager


def view_all_contacts():
    contacts = manager.get_all()
    for contact in contacts:
        print(contact.first_name, contact.last_name, contact.phone)
