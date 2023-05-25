import BeginnerLessons.ContactDir.contact_manager as manager
import BeginnerLessons.ContactDir.impl as impl
from BeginnerLessons.ContactDir.contact import Contact


def delete_contact(contact):
    manager.delete(contact)
    print('contact deleted successfully')
    impl.init()


def find_contact(first_name):
    contacts = manager.get_all()
    for contact in contacts:
        if contact.first_name == first_name:
            return contact
        else:
            return None


def check(contact: Contact):
    response = input(f"Are you sure you want to delete \n"
                     f"{contact.first_name, contact.last_name, contact.phone}? YES/NO")
    match response:
        case 'YES':
            delete_contact(contact)
        case 'NO':
            print('operation cancelled')
            impl.init()


def start():
    first_name = input('Enter first name to delete:')
    if not first_name:
        raise ValueError('please enter a valid first name')
    contact = find_contact(first_name)
    if contact:
        check(contact)
    else:
        print(f'No contact matching {first_name} was found')
        impl.init()
