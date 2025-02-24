from database import *

class Customer:
    def __init__(self, username, password, name,email, age, city, account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email=email
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createuser(self):
        query = (f"INSERT INTO customers (username, password, name, email,age, city,balance, account_number, status) "
                 f"VALUES ('{self.__username}', '{self.__password}', '{self.__name}','{self.__email}', "
                 f"'{self.__age}', '{self.__city}', 0,'{self.__account_number}', True)")
        cursor.execute(query)
        mydb.commit()


