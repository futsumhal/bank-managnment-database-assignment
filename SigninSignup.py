import random
from database import *
from User import *
import smtplib
from bank_system import *
from werkzeug.security import generate_password_hash,check_password_hash

my_emal="futsumhal@gmail.com"
password="ybexcscncdvnkyrf"
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
                user_email = db_query(f"SELECT email FROM customers WHERE username='{username}';")
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_emal, password=password)
                connection.sendmail(from_addr=my_emal,
                                    to_addrs=user_email,
                                    msg=f"Subject:HEllo\n\nDear {username} your account Registered  successfully.Thank you for Banking with us.")
                break

    cusobj = Customer(username, hashed_password, name,email, age, city, account_number)
    cusobj.createuser()
    connection.close()
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


