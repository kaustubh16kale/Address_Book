import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',filename="Address.log",level=logging.INFO)

def show_details(first_name,last_name,address,city,zip,phone_number,email):
    print(f"First name is: {first_name} ,Last name is: {last_name}, Address is : {address}, city is : {city}, zip code is : {zip}, phone number is : {phone_number}, Email is {email}")

def detail_input():
    first_name=str(input("Enter the first name  : "))
    last_name=str(input("Enter the last name : "))
    address=input("Enter the address : ")
    city=input("Enter the city : ")
    zip=input("Enter the zip code: ")
    phone_number=int(input("Enter the phone number : "))
    email=input("Enter the email : ")
    show_details(first_name,last_name,address,city,zip,phone_number,email)

def main():
    try:
        detail_input()
    except Exception as e:
        logger.exception(e)


if __name__=="__main__":
    main()