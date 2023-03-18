import smtplib
import csv

from email.message import Message


def sendEmail(name, toAddr):
    print(name, toAddr)
    sender = "[EMAIL ADDRESS]"  # Input the users email address here
    password = "[MAIL PASSWORD]"  # Input the users password here

    subject = '[SUBJECT]'  # Input the subject title of the email

    # This program pulls a message out of a text document.
    # This text document is formatted to display better in an email format.
    fileMessage = open("./venv/Message.txt").read()  # make sure to update the message.txt file

    # Read in file message
    message = fileMessage

    # Create a email message
    msg = Message()
    msg['Subject'] = subject
    msg.set_payload(message.format(name))
    text = msg.as_string()

    # Calls the callMail() function to send email
    callMail(sender, password, toAddr, text)


def getAddr():
    # Defined these variables in case contact.txt doesn't exist.
    MemberName = "[DEFAULT NAME]"  # Might want to define default creds
    emailAddr = "[DEFAULT EMAIL ADDRESS]"  # Might want to define default creds

    # Open Contact.txt
    file = open("./venv/Contact.txt")  # make sure to edit the Contact.txt file and input target email addresses

    # Read in file delimited by Name,Email Address
    reader = csv.reader(file, delimiter=',')

    # Input contents of file into correct var
    for row in reader:
        MemberName = row.__getitem__(0)
        emailAddr = row.__getitem__(1)

        # Call the send email function to format and send the email.
        sendEmail(MemberName, emailAddr)


def callMail(sender, password, toAddr, message):
    # Create a connection, login, and send the desired message using the format
    # provided by sendEmail()
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender, to_addrs=toAddr, msg=message, )
    connection.close()


if __name__ == '__main__':
    getAddr()
