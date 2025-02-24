import sys
from database import *
from SigninSignup import *
from bank_system import *
import smtplib
print("Bank Mangnment system project")
my_emal="dbbank.11@gmail.com"
password="tjcpdtspmbwgdwqu"
password="tjcpdtspmbwgdwqu"
status=True


while True:
    try:
        register=int(input("1. SignUp              2, SignIn       3,Exit\n"))
        if register==1 or register==2 or register==3:
            if register==1:
                SignUP()
            elif register==2:
                user=SignIn()
                status=True
                break
            elif register==3:
                quit()




        else:
            print("please Enter Correct Input")

    except ValueError:
        print("Invalid Input Try Again with Numbers")
account_number=db_query(f"SELECT account_number FROM customers WHERE username='{user}';")
user_email=db_query(f"SELECT email FROM customers WHERE username='{user}';")


while status:
    print(f"Welcome {user.capitalize()} choose your banking system")
    try:
        facility=int(input("1. Balance Enquiry  2, Cash Deposit   3, Cash withdraw  4, Fund Transfer    5, Exit\n"))
        if facility>=1 and facility<=5:

            if facility==1:
                baob = Bank(user, account_number[0][0])
                baob.balancequery()
            elif facility==2:
                while True:
                    try:
                        amount = int(input("Enter amount to deposit"))
                        baob = Bank(user, account_number[0][0])
                        baob.deposit(amount)
                        mydb.commit()
                        balance = db_query(f"SELECT balance FROM customers WHERE username='{user}';")
                        connection = smtplib.SMTP_SSL("smtp.gmail.com")
                        connection.login(user=my_emal, password=password)
                        connection.sendmail(from_addr=my_emal,
                                            to_addrs=user_email,
                                            msg=f"Subject:Deposit Confirmation-Account{account_number[0][0]}\n\nDear {user}.\nWe are pleased to inform you that a deposit ETB{amount} has been successfully made to your account{account_number[0][0]}.Your Current Balance is ETB{balance[0][0]}.Thank you for Banking with BBANK.")
                        connection.close()
                        break
                    except ValueError:
                        print("Enter valid input ie,number")
                        continue

            elif facility == 3:
                while True:
                    try:
                        balance = db_query(f"SELECT balance FROM customers WHERE username='{user}';")
                        amount = int(input("Enter amount to withdraw"))
                        if amount>balance[0][0]:
                            print("Insufficent Balance.please Enter valid amount")
                            continue
                        baob = Bank(user, account_number[0][0])
                        baob.withdraw(amount)
                        mydb.commit()
                        balance = db_query(f"SELECT balance FROM customers WHERE username='{user}';")
                        connection = smtplib.SMTP_SSL("smtp.gmail.com")
                        # connection.starttls()
                        connection.login(user=my_emal, password=password)
                        connection.sendmail(from_addr=my_emal,
                                            to_addrs=user_email,
                                            msg=f"ubject:Withdraw Confirmation-Account{account_number[0][0]}\n\nDear {user}.\nThis is to notify you that a Withdrawal of  ETB{amount} has been made successfully from your account{account_number[0][0]}.Your Current Balance is ETB{balance[0][0]}.Thank you for Banking with BBANK.")
                        connection.close()
                        break
                    except ValueError:
                        print("Enter valid input ie,number")
                        continue

            elif facility == 4:
                while True:
                    try:
                        balance = db_query(f"SELECT balance FROM customers WHERE username='{user}';")
                        amount = int(input("Enter  amount to transfer: "))
                        if amount > balance[0][0]:
                            print("Insufficent Balance.please Enter valid amount")
                            continue
                        receiver = int(input("Enter Reciever Account Number"))
                        temp = db_query(f"SELECT account_number FROM customers WHERE account_number='{receiver}';")
                        if temp:
                            print("Account number exists proceedings...")
                            baob = Bank(user, account_number[0][0])
                            baob.fund_transfer(receiver, amount)
                            mydb.commit()
                            balance = db_query(f"SELECT balance FROM customers WHERE username='{user}';")
                            balance2 = db_query(f"SELECT balance FROM customers WHERE account_number='{receiver}';")[0][0]
                            user2 = db_query(f"SELECT username FROM customers WHERE account_number='{receiver}';")[0][0]
                            user2_email = db_query(f"SELECT email FROM customers WHERE account_number='{receiver}';")
                            connection = smtplib.SMTP_SSL("smtp.gmail.com")
                            # connection.starttls()
                            connection.login(user=my_emal, password=password)
                            connection.sendmail(from_addr=my_emal,
                                                to_addrs=user_email,
                                                msg=f"Subject:Fund Transfer Confimation - Account{account_number[0][0]}\n\nDear {user}.\n We are pleased to inform you that your fund transfer request  ETB{amount} has been successfully processed.Your Current Balance is ETB{balance[0][0]}.Thank you for Banking with BBANK.")
                            connection.sendmail(from_addr=my_emal,
                                                to_addrs=user2_email,
                                                msg=f"Subject:Fund Receipt Confirmation - Account{receiver} \n\nDear {user2}.\n We are pleased to inform you that ETB{amount} has been successfully received in your account-{receiver} .Your Current Balance is ETB{balance2}.Thank you for Banking with us.")
                            connection.close()

                            break
                        else:
                            print("Account number Doesn't exist. Please enter correct Account number")
                            continue

                    except ValueError:
                        print("Enter valid input ie,number")
                        continue

            elif facility==5:
                sys.exit()


        else:
            print("please Enter Correct Input")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue
