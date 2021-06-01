# THis Can Be Used To Send Emails TO Customer For Promotional Offers
import smtplib, ssl


f = open("emails.txt",'r')
content = f.read()
content = content.split("\n")
receiver_email = content[0]
f.close()


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "atlvvdavtest@gmail.com"  # Enter your address
password = input("Type your password and press enter: ")
message = (open("message.txt",'r').read())

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)