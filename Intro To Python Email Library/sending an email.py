import smtplib
import getpass
import os.path
import mimetypes
from email.message import EmailMessage
message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greetings from {} to {}!".format(sender, recipient)
body = "Hello There." \
       "..." \
       "..." \
       "I'm learning to send emails through Python"
message.set_content(body)
print(message)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_pass = getpass.getpass('Password? ')
print(mail_pass)
mail_server.set_debuglevel(1)
mail_server.login(sender, mail_pass)