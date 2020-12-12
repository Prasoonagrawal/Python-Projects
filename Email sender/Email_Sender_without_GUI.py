import smtplib
sender=input("Enter sender Email: ")
passw=input("Enter you Email password: ")
reciver=input("Enter reciver Emails (space sperated):  ")

content=input("Enter Your Message: ")

print("login start")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,passw)
print("login success")
server.sendmail(sender,reciver.split(','),content)
print("Email sent")
server.close()

