import random
from database import *
from User import *
import smtplib
from bank_system import *
from werkzeug.security import generate_password_hash,check_password_hash
my_emal="dbbank.11@gmail.com"
email_password="tjcpdtspmbwgdwqu"
def SignUP():
    username = input("create username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username='{username}';")
    if temp:
        print("username already exists")
        SignUP()
    else:
        print("username is available, please proceed")
        password = input("Enter your password: ")
        hashed_password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        age = input("Enter your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number='{account_number}';")
            if temp:
                continue
            else:
                print(f"This Is Your Account_number{account_number}")
                connection = smtplib.SMTP_SSL("smtp.gmail.com")
                connection.login(user=my_emal, password=email_password)
                connection.sendmail(from_addr=my_emal,
                                    to_addrs=email,
                                    msg=f"Subject:WELCOME TO BBANK\n\nWe are pleased to inform you that your account has been successfully created at BBANK. Your account number is {account_number}. .Thank you for choosing BBANK as your Trusted financial partner.")
                connection.close()
                break

    cusobj = Customer(username, hashed_password, name,email, age, city, account_number)
    cusobj.createuser()

    baobj=Bank(username,account_number)
    baobj.create_transaction_table()



def SignIn():
    username = input("Enter username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username='{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter password: ")
            temp = db_query(f"SELECT password FROM customers WHERE username='{username}';")
            stored_password=temp[0][0]
            if check_password_hash(stored_password,password):
                print("Success! You've Signed IN Successfully")
                return username
            else:
                print("please Enter Valid Password")
                continue
    else:
        print("Entere Correct Username")
        SignIn()


