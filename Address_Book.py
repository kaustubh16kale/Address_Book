import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Address.log",
                    level=logging.INFO)

user_list=[] # list to store the object 

class Address_Book:
    def __init__(self,name):
        self.name=name
        self.contact=[]

    def add_contact(self,first_name):
        contact = {
            'first_name': first_name,
            'last_name': input("Enter the last name: "),
            'address': input("Enter the address: "),
            'city': input("Enter the city: "),
            'zip': int(input("Enter the zip code: ")),
            'phone_number': int(input("Enter the phone number: ")),
            'email': input("Enter the email: ")
        }
        self.contact.append(contact)
        print("Contact added successfully.")
    
    def show_details(self):
        if self.contact:
            for contact in self.contact:
                print(f"First name: {contact['first_name']}, "
                      f"Last name: {contact['last_name']}, "
                      f"Address: {contact['address']}, "
                      f"City: {contact['city']}, "
                      f"Zip code: {contact['zip']}, "
                      f"Phone number: {contact['phone_number']}, "
                      f"Email: {contact['email']}")
        else:
            print("No contacts found.")
    
    def change_details(self,first_name):
        for contact in self.contact:
            if contact['first_name'] == first_name:
                print("Enter new details:")
                contact['last_name'] = input(f"Last name ({contact['last_name']}): ")
                contact['address'] = input(f"Address ({contact['address']}): ")
                contact['city'] = input(f"City ({contact['city']}): ")
                contact['zip'] = int(input(f"Zip code ({contact['zip']}): "))
                contact['phone_number'] = int(input(f"Phone number ({contact['phone_number']}): "))
                contact['email'] = input(f"Email ({contact['email']}): ")
                print("Contact updated successfully.")
                break
        else:
            print("Contact not found.")
    
    def delete_info(self,input_name):
        for contact in self.contact:
            if contact['first_name'] == input_name:
                self.contact.remove(contact)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")

def main():
    address_book_dictionary={} #dictionary to store address book names
    while True:
        try:
            print("Press ENTER to close the programm : \n Enter 1 to add new address book \n Enter 2 to select existing address book : ")
            input_choice=int(input("Enter the choice: "))
            match input_choice:
                case 1:
                    name = input("Enter the name of the new address book: ")
                    if name not in address_book_dictionary:
                        address_book_dictionary[name] = Address_Book(name)
                        print("Address book created successfully.")
                    else:
                        print("An address book with that name already exists.") 
                case 2:
                        for books in address_book_dictionary.keys():
                            print(books,end="  ")
                            print()
                        name = input("Enter the name of the address book: ")
                        address_book = address_book_dictionary.get(name)
                        if address_book:
                            while True:
                                print("\nEnter 0 to return to the main menu.")
                                print("Enter 1 to add a new contact.")
                                print("Enter 2 to show all contacts.")
                                print("Enter 3 to edit a contact.")
                                print("Enter 4 to delete a contact.")
                                option = int(input("Enter your option: "))

                                if option == 0:
                                    break

                                match option:
                                    case 1:
                                        first_name = input("Enter the first name: ")
                                        address_book.add_contact(first_name)

                                    case 2:
                                        address_book.show_details()

                                    case 3:
                                        first_name = input("Enter the first name of the contact to edit: ")
                                        address_book.change_details(first_name)

                                    case 4:
                                        first_name = input("Enter the first name of the contact to delete: ")
                                        address_book.delete_info(first_name)

                        else:
                            print("Address book not found.")  
                case _ :
                    break

        except Exception as e:
            logger.exception(e)


if __name__=="__main__":
    main()