from parser import parsefile
import smtplib, ssl
from MailDeets import MailDeets

"""
MailDeets.py

class MailDeets:
    def __init__(self):
        self.mymail = 'your-gmail-id'
        self.password = 'your-password'
"""

# get the filepath to the data
filepath = './data/data.csv'

mailinfo = MailDeets() # instantiate an object of the MailDeets class. (not included in the repo)
sender = mailinfo.mymail # the self.mymail attribute has the mail id of the sender
password = mailinfo.password # the self.password attribute contains the password for accessing the smtp server

# receiver = sender # for testing purposes only

subject = 'add the subject here'
body = """
    add the message body here
"""
msg = 'Subject: ' + subject + '\n' + body

receivers = parsefile(filepath) # parses the entire dataset into a list of email addresses (change as per schema of dataset)
PORT = 465 # assign smtp port
sslcontext = ssl.create_default_context()
connection = smtplib.SMTP_SSL("smtp.gmail.com",PORT,context=sslcontext)

connection.login(sender, password) # login to smtp server

i = 0 # counter for number of mails sent. After 85 or so, the server logs you out for 2 mins, gotta log in and start again
for rec in receivers:
    connection.sendmail(sender, rec, msg)
    print(str(i) + ": Message sent!!") # confirmation message
    i = i+1