import json


class ContactList:
    def __init__(self, filepath="contactlist.json"):
        self.filepath = filepath

    def add_contact(self, name, address, phone_number):
        contact_format = {
            "name": f"{name}",
            "address": f"{address}",
            "phone_number": f"{phone_number}"
        }
        with open(self.filepath, 'r+') as jsfile:
            contact_list = json.load(jsfile)
            for contact in contact_list:
                if contact['name'] == name or contact['address'] == address or contact['phone_number'] == phone_number:
                    if input(
                            "there is a contact with similar info,are you sure you want to add this one (y or n)") != 'y':
                        print("canceled")
                        return

            contact_list.append(contact_format)
            jsfile.seek(0, 0)
            js_format = json.dumps(contact_list, indent=4)
            jsfile.write(js_format)
            return f"added {name} to contact list"

    def search(self, search):
        with open(self.filepath, 'r') as jsfile:
            contact_list = json.load(jsfile)
            for contact in contact_list:
                if contact['name'] == search or contact['address'] == search or contact['phone_number'] == search:
                    return contact
            return -1

    def isContact(self, search):
        with open(self.filepath, 'r') as jsfile:
            contact_list = json.load(jsfile)
            for contact in contact_list:
                if contact['name'] == search or contact['address'] == search or contact['phone_number'] == search:
                    return True
            return False

    def delete_contact(self, search):
        with open(self.filepath, 'r') as jsfile:
            contact_list = json.load(jsfile)

            for contact in contact_list:
                if contact['name'] == search or contact['address'] == search or contact['phone_number'] == search:
                    contact_list.remove(contact)

            print(contact_list)
            with open(self.filepath, 'w') as f:
                json.dump(contact_list, f)

    def print_list(self):
        with open(self.filepath, 'r') as jsfile:
            contact_list = json.load(jsfile)
            for contact in contact_list:
                print(f"\nName: {contact['name']}\n"
                      f"Address: {contact['address']}\n"
                      f"Phone Number: {contact['phone_number']}\n"
                      f"Other Info: \n")

    def clear_list(self):
        with open(self.filepath, 'r') as jsfile:
            contact_list = json.load(jsfile)
            for contact in contact_list:
                contact_list.remove(contact)

        print(contact_list)
        with open(self.filepath, 'w') as f:
            json.dump(contact_list, f)
