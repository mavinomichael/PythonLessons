import BeginnerLessons.ContactDir.contact_manager as manager
import BeginnerLessons.ContactDir.impl as impl


def view_all_contacts():
    contacts = manager.get_all()
    for contact in contacts:
        print(contact.first_name, contact.last_name, contact.phone)
        impl.init()

