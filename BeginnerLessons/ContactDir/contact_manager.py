from BeginnerLessons.ContactDir.contact import Contact

contacts: [Contact] = []


def add(contact: Contact):
    contacts.append(contact)


def delete(contact: Contact):
    contacts.remove(contact)


def get_all():
    return contacts


"""
The search feature is based on
A linear search algorithm
"""


def search(query):
    results = []
    query = query.lower()
    for contact in contacts:
        first_name = contact.first_name
        last_name = contact.last_name

        if query in first_name or query in last_name:
            results.append(contact)

    return results
