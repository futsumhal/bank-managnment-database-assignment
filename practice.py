import smtplib
my_emal="futsumhal@gmail.com"
password="vynrnfsaibxrhlyz"

connection = smtplib.SMTP("smtp.gmail.com")
print("futsu")
connection.starttls()
print("futsu")
connection.login(user=my_emal, password=password)
connection.sendmail(from_addr=my_emal,
                    to_addrs="futsumhalefm@gmail.com",
                    msg=f"Subject:HElloDear futsum your account 879878 has been Credited wit successfully.Your Current Balance is ETBhank you for Banking with us.")
connection.close()