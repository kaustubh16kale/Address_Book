import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename="Address.log",
                    level=logging.INFO)

class Address_Book:
    def __init__(self):
        self.first_name=input("Enter the first name  : ")
        self.last_name=input("Enter the last name : ")
        self.address=input("Enter the address : ")
        self.city=input("Enter the city : ")
        self.zip=int(input("Enter the zip code: "))
        self.phone_number=int(input("Enter the phone number : "))
        self.email=input("Enter the email : ")
    
    def show_details(self):
        print(f"First name is: {self.first_name}, "
              f"Last name is: {self.last_name}, " 
              f"Address is : {self.address}, " 
              f"city is : {self.city}, " 
              f"zip code is : {zip}, " 
              f"phone number is : {self.phone_number}, " 
              f"Email is: {self.email}, ")

def main():
    try:
        person1=Address_Book()
        person1.show_details()
    except Exception as e:
        logger.exception(e)


if __name__=="__main__":
    main()