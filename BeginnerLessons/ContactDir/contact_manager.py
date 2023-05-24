from BeginnerLessons.ContactDir.contact import Contact

contacts: [Contact] = []


def add(contact: Contact):
    contacts.append(contact)


def delete(contact: Contact):
    contacts.remove(contact)


def get_all():
    return contacts
