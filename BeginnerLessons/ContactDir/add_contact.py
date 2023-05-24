import BeginnerLessons.ContactDir.contact_manager as manager
from BeginnerLessons.ContactDir.contact import Contact
import BeginnerLessons.ContactDir.impl as impl


def add_contact(first_name, last_name, phone):
    contact = Contact(first_name, last_name, phone)
    manager.add(contact)


def start():
    first_name = input('first name:')
    if not first_name:
        raise ValueError('please enter a valid first name')
    last_name = input('last name:')
    if not last_name:
        raise ValueError('please enter a valid last name')
    phone = int(input('phone:'))
    if not phone:
        raise ValueError('please enter a valid phone')
    add_contact(first_name, last_name, phone)
    impl.init()

