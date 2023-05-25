import BeginnerLessons.ContactDir.contact_manager as manager
from BeginnerLessons.ContactDir import impl
from BeginnerLessons.ContactDir.contact import Contact


def show(results: [Contact]):
    for contact in results:
        print(f'{contact.first_name, contact.last_name, contact.phone}')

    impl.init()


def start():
    query = input('Enter your search query:')
    if not query:
        raise ValueError('please enter a valid first name')
    result = manager.search(query)
    if result:
        show(result)
    else:
        print(f'No contact matching {query} was found')
        impl.init()
