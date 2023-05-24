import BeginnerLessons.ContactDir.add_contact as add_manager
import BeginnerLessons.ContactDir.delete_contact as delete_manager
import BeginnerLessons.ContactDir.view_contacts as view_manager


def init():
    response = int(input("1. Add a new contact \n"
                         "2. View all contacts \n"
                         "3. Search for a contact \n"
                         "4. Delete a contact \n"
                         "5. Exit \n"
                         "Input here: "))
    match response:
        case 1:
            add_manager.start()
        case 2:
            view_manager.view_all_contacts()
        case 3:
            add_manager.start()
        case 4:
            delete_manager.start()
        case 5:
            print('Goodbye!')
