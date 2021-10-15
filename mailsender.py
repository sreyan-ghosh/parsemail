from parser import parsefile
import smtplib, ssl
from MailDeets import MailDeets

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
MailDeets.py

class MailDeets:
    def __init__(self):
        self.mymail = 'your-gmail-id'
        self.password = 'your-password'
        self.teamsusername = 'teamsusername'
"""

# get the filepath to the data
filepath = './data/data.csv'
attachmentfile = input("Path of file to attach (leave empty for no attachment): ")

mailinfo = MailDeets() # instantiate an object of the MailDeets class. (not included in the repo)
sender = mailinfo.mymail # the self.mymail attribute has the mail id of the sender
password = mailinfo.password # the self.password attribute contains the password for accessing the smtp server

# receiver = sender # for testing purposes only

subject = 'add the subject here'
body = """
    add the message body here
"""

message = MIMEMultipart()

message["From"] = sender
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

receivers = parsefile(filepath) # parses the entire dataset into a list of email addresses (change as per schema of dataset)
PORT = 465 # assign smtp port
sslcontext = ssl.create_default_context()
connection = smtplib.SMTP_SSL("smtp.gmail.com",PORT,context=sslcontext)

connection.login(sender, password) # login to smtp server

try:
    with open(attachmentfile, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachmentfile}",)

    message.attach(part)

except Exception as e:
    if attachmentfile:
        print("Error opening attached file. Check the file path and permissions")
        ans = input("Continue without attaching file? (y/N)")
        if ans in ["n", "N"]:
            exit()
        elif ans not in ["y", "Y"]:
            print("Unexpected input, exiting")
            exit(1)


message = message.as_string()

i = 1 # counter for number of mails sent. After 85 or so, the server logs you out for 2 mins, gotta log in and start again
for rec in receivers:
    connection.sendmail(sender, rec, message)
    print(str(i) + ": Message sent!!") # confirmation message
    i = i+1