import logging
import json

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Address.log",
                    level=logging.INFO)

user_list=[] 

class Address_Book:
    def __init__(self,name):
        '''
        Function: Constructor for creating object of address book
        Parameter: Self,Name:Name of the Address book 
        Return : None
        '''
        self.name=name
        self.contact=[]

    def add_contact(self,first_name):
        '''
        Function: add_contact: Function to add contact in the address book
        Parameters: first_name: first_name of the contact
        Return: None
        '''
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
        '''
        Function: show_details: Function used to print the detail of the address book
        Parameter: self: reference to the object of the address book
        Return: None
        '''
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
        '''
        Function: change_detail: Function to change the existing detail of the contact
        Parameters: self,first_name: first_name- name of the user
        Return : None
        '''
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
        '''
        Function: delete_info: Function to delete the information of the contact
        Parameters: self: self reference object
                    input_name: refered as first_name of the contact
                    last_name:  refered as the last name of the contact
        Return: None
        '''
        for contact in self.contact:
            if contact['first_name'] == input_name and contact['last_name']==last_name:
                self.contact.remove(contact)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")
    
    def search_city(self,check_city):
        '''
        Function: search_city: Function to check the total number of contact from particular city
        Parameters: self: self reference object
                    check_city: name of the city (user input)
        Return : Total count of the contacts from particular city
        '''
        count=0
        for contact in self.contact:
            if contact['city']==check_city:
                print(f"{contact['first_name']} {contact['last_name']}")
                count+=1
        else:
            print(f"No contact from {check_city} city ")  # to check later
        print(f"{count} contact founds from city {check_city}")
    
    def sort_contact(self):
        '''
        Function: sort_contact: Function used to sort the existing contacts according to the user parameters
        Parameters: self: self reference object
        Return : Sorted contacts from the address book
        '''
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
        '''
        Function: save_to_file: Function to save the address book
        Parameters: self: self reference object
                    filename: user input name of the file as which the address book is to be saved
        Return: None
        '''
        with open(filename, 'w') as file:
            json.dump(self.contact, file)
        print(f"Contacts of address book '{self.name}' saved to file '{filename}' successfully.")
    
    def load_from_file(self, filename):
        '''
        Function: load_from_file: Function to load the existing saved file
        Parameters: self: self reference object
                    filename: name of the address book to be load
        Return: None
        '''
        try:
            with open(filename, 'r') as file:
                self.contact = json.load(file)
            print(f"Contacts loaded from file '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            logger.exception(FileNotFoundError)

def main():
    '''
    Function: main
    Parameters: None
    Return: None
    '''
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