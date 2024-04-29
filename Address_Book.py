import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Address.log",
                    level=logging.INFO)

user_list=[] # list to store the object 

class Address_Book:
    def __init__(self,first_name):
        self.first_name=first_name
        self.last_name=input("Enter the last name : ")
        self.address=input("Enter the address : ")
        self.city=input("Enter the city : ")
        self.zip=int(input("Enter the zip code: "))
        self.phone_number=int(input("Enter the phone number : "))
        self.email=input("Enter the email : ")
        user_list.append(self)
        main()
    
    def show_details(self):
        print(f"First name is: {self.first_name}, "
              f"Last name is: {self.last_name}, " 
              f"Address is : {self.address}, " 
              f"city is : {self.city}, " 
              f"zip code is : {self.zip}, " 
              f"phone number is : {self.phone_number}, " 
              f"Email is: {self.email}, ")
        return main()
    
    def change_details(self):
        name_update=input(f"Enter the new name for the contact {self.first_name} : ")
        self.first_name=name_update
        print("Name changed ")
        return main()
    
    def delete_info(self,input_name):
        for user in user_list:
            if user.first_name==input_name:
                user_list.remove(user)
                print("Contact deleted ")
                break
        else:
            print("Contact not found ")
        return main()

def main():
    while True:
        try:
            input_user=int(input("Enter 0 to close the programm : \nEnter 1 to add user :  \n Enter 2 to edit user : \n Enter 3 to check the details of the contact: \n Enter 4 to delete the existing contact: "))
            if input_user==0:
                break
            match(input_user):
                case 1:
                    new_user=input("Enter the first_name of the user")
                    new_user=Address_Book(new_user)
                    # user_list.append(new_user) #storing object in the list
                case 2:
                    name_update=input("Enter the name of the contact to change the info: ")
                    for user in user_list:
                        if user.first_name==name_update:
                            user.change_details()
                            break
                    else:
                        print("contact not found")
                case 3:
                    input_name=input("Enter the name of the user to check the details: ")
                    for user in user_list:
                        if user.first_name==input_name:
                            user.show_details()
                            break
                    else:
                        print("Contact not found ")
                case 4:
                    input_name=input("Enter the name of the contact to delete the info : ")
                    for user in user_list:
                        if user.first_name==input_name:
                            user.delete_info(input_name)
                    else:
                        print("Contact not found ")

        except Exception as e:
            logger.exception(e)


if __name__=="__main__":
    main()