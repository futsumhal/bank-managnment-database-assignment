from database import *
import datetime
class Bank:


    def __init__(self,username,account_number):
        self.__username= username
        self.__account_number=account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOt EXISTS {self.__username}_transaction"
                 f"(timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER)")

    def balancequery(self):
        ubalance= db_query(f"SELECT balance From customers WHERE username='{self.__username}';")
        print(f"Dear {self.__username} Your Account Balance is ETB{ubalance[0][0]}.")


    def deposit(self,amount):
        temp=db_query(f"SELECT balance From customers WHERE username='{self.__username}';")
        test=temp[0][0]+amount
        db_query(f"UPDATE customers SET balance='{test}' WHERE username='{self.__username}';")
        self.balancequery()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{amount} is successfully deposited into your account{self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance From customers WHERE username='{self.__username}';")
        if amount>temp[0][0]:
            print("insufficent Balance  please deposit money")
        else:
            test=temp[0][0] - amount
            db_query(f"UPDATE customers SET balance='{test}' WHERE username='{self.__username}';")
            self.balancequery()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount withdraw',"
                     f"'{amount}'"
                     f")")
            print(f"{amount} is successfully withdrawed  from your account{self.__account_number}")

    def fund_transfer(self,receiver, amount):
        temp= db_query(f"SELECT balance FROM customers WHERE username='{self.__username}';")
        if amount > temp[0][0]:
            print("insufficent Balance  please deposit money")
        else:
            temp2=db_query(f"SELECT balance FROM customers WHERE account_number = '{receiver}';")
            test=temp[0][0] - amount
            test2=temp2[0][0] + amount
            db_query(f"UPDATE customers SET balance='{test}' WHERE username='{self.__username}';")
            db_query(f"UPDATE customers SET balance='{test2}' WHERE account_number='{receiver}';")
            receiver_username=db_query(f"SELECT username FROM customers WHERE account_number= '{receiver}';")
            self.balancequery()
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'fund transfer from {self.__account_number}',"
                     f"'{amount}'"
                     f")")
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'fund transfer -->{receiver}',"
                     f"'{amount}'"
                     f")")


            print(f"{amount} is successfully transfered  from your account{self.__account_number}")

