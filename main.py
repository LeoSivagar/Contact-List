from ContactList import ContactList

cont = True
contactlist = ContactList()
contactlist.add_contact("Bob", "123 Somewhere Rd", "123 123 2134")
contactlist.add_contact("Ryan", "123 Nowhere Avenue", "121 123 1234")
contactlist.add_contact("Leo", "123 Arastradero Rd", "131 123 3123")

print("Hello! Welcome to Contact List\ntype \"help\" for commands")
while cont:
    uInput = input("> ")
    if uInput == "help":
        print("\nadd-contact - adds new contact to the contact list\n"
              "find-contact - finds contact with search prompt\n"
              "print-list - prints entire contact list\n"
              "delete-contact - deletes contact\n"
              "empty-list - empties the contact list\n")
    elif uInput == "add-contact":
        name = input("What is their name? ")
        address = input("What is their address? ")
        phone_number = input("What is their phone number?")
        contactlist.add_contact(name, address, phone_number)
    elif uInput == "find-contact":
        search = input("Search prompt? ")
        if contactlist.search(search) == -1:
            print("Person is not in contacts")
        else:
            print(f"\nName: {contactlist.search(search)['name']}\n"
                  f"Address: {contactlist.search(search)['address']}\n"
                  f"Phone Number: {contactlist.search(search)['phone_number']}\n"
                  f"Other Info: \n")
    elif uInput == "print-list":
        contactlist.print_list()
    elif uInput == "delete-contact":
        search = input("Who do you want to delete? ")
        if contactlist.isContact(search):
            contactlist.delete_contact(search)
        else:
            print("Contact does not exist")
    elif uInput == "empty-list":
        contactlist.clear_list()
    elif uInput == "exit":
        cont = False
    else:
        print("input unknown, try again")











