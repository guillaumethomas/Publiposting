"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
from getpass import getpass
from email.message import EmailMessage


def main():

    print("This is a script to send email")
    gmail_user = 'guillaume.ronan.thomas@gmail.com'
    gmail_password = getpass('Password ?\n')

    to = ["guillaumethomas@outlook.com"]
    subject = "Git HUB"
    content = "Salut!\n \nVas sur Git HUB! \n \n https://github.com/guillaumethomas/Publiposting \n " \
              "\n Sent from a Python Script"

    server = connection_server(gmail_user,gmail_password)

    for address in to:
        msg = mail_o(content,subject,gmail_user,address)
        # server.sendmail(sent_from, address, email_text)
        server.send_message(msg)

    server.close()
    exit("Email sent")


def connection_server(username, password):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username,password)
    except:
        exit("Bad Connection or Bad Password => email not sent")

    return server


def mail_o(content, subject, sender, recipient):

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    return msg


if __name__ == "__main__":
    main()
