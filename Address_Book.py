import logging
import json

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Address.log",
                    level=logging.INFO)

user_list=[] # list to store the object 

class Address_Book:
    def __init__(self,name):
        self.name=name
        self.contact=[]  # list used to store multiple dictionaries of contacts

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
        self.contact.append(contact)  # appending dictionaries to contact list
        print("Contact added successfully.")
    
    def show_details(self):
        if self.contact:
            sorted_contacts = sorted(self.contact, key=lambda x: x['first_name'])  #lambda function to sort the contacts based on first_name
            for contact in sorted_contacts:
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
    
    def delete_info(self,input_name,last_name):
        for contact in self.contact:
            if contact['first_name'] == input_name and contact['last_name']==last_name:
                self.contact.remove(contact)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")
    
    def search_city(self,check_city):  # return the count of the contacts form particular city
        count=0
        for contact in self.contact:
            if contact['city']==check_city:
                print(f"{contact['first_name']} {contact['last_name']}")
                count+=1
        else:
            print(f"No contact from {check_city} city ")  # to check later
        print(f"{count} contact founds from city {check_city}")
    
    def sort_contact(self):
        print("1 to sort by first_name \n 2 to sort by last_name \n 3 to sort by city \n ")
        sort_check=int(input("Enter your choice to sort : "))
        if sort_check==1:
            sort_check="first_name"
        elif sort_check==2:
            sort_check="last_name"
        elif sort_check==3:
            sort_check="city"
        else:
            print("invalid input")
            return
        if self.contact:
            sorted_contacts = sorted(self.contact, key=lambda x: x[sort_check])  #lambda function to sort the contacts based on user_input
            for contact in sorted_contacts:
                print(f"First name: {contact['first_name']}, "
                    f"Last name: {contact['last_name']}, "
                    f"Address: {contact['address']}, "
                    f"City: {contact['city']}, "
                    f"Zip code: {contact['zip']}, "
                    f"Phone number: {contact['phone_number']}, "
                    f"Email: {contact['email']}")
        else:
            print("No contacts to sort")
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contact, file)
        print(f"Contacts of address book '{self.name}' saved to file '{filename}' successfully.")
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contact = json.load(file)
            print(f"Contacts loaded from file '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

def main():
    address_book_dictionary={} #dictionary to store address book names
    while True:
        try:
            print("Press ENTER to close the programm : \n Enter 1 to add new address book \n Enter 2 to select existing address book : /n Enter 3 to save all the address book in file : /n Enter 4 to load the address books from the saved file : ")
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
                                print("Enter 5 to search the person based on city: ")
                                print("6.sort contacts: ")
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
                                        last_name=input("Enter the last name of the contact: ")
                                        address_book.delete_info(first_name,last_name)
                                    
                                    case 5:
                                        check_city=input("Enter a city name to search details : ")
                                        address_book.search_city(check_city)
                                    
                                    case 6:
                                        # sort_check=input("Enter the factor to sort the contacts based on: i:e(city,zip): ")
                                        address_book.sort_contact()          
                        else:
                            print("Address book not found ")  
                case 3:
                    for name, address_book in address_book_dictionary.items():
                        filename = f"{name}.json"
                        address_book.save_to_file(filename)
                    print("All address books saved successfully.")
                
                case 4:
                    name = input("Enter the name of the address book to load from file: ")
                    filename = f"{name}.json"
                    address_book = Address_Book(name)
                    address_book.load_from_file(filename)
                    address_book_dictionary[name] = address_book
                
                case _ :
                    break

        except Exception as e:
            logger.exception(e)


if __name__=="__main__":
    main()