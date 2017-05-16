"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
from email.message import EmailMessage


def main():

    print("This is a script to send email")
    gmail_user = 'guillaume.ronan.thomas@gmail.com'
    gmail_password = input('Password ?\n')

    to = ["guillaumethomas@outlook.com","sterennr@hotmail.com"]
    subject = "Test Python"
    content="Coucou Mon Panda\nJe fais un test en python\n \nBisous\nTon Loup"

    server_t = connection_server(gmail_user,gmail_password)
    if server_t[0] == True:
        server = server_t[1]

    msg = mail_o(content,subject,gmail_user,to)

    #server.sendmail(sent_from, to, email_text)
    server.send_message(msg)
    server.close()


def connection_server(username, password):

    bool=True
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username,password)
    except:
        print('Something went wrong...')
        bool=False

    return bool, server


def mail_o(content, subject, sender, recipient):

    msg=EmailMessage()
    msg.set_content(content)
    msg['Subject']=subject
    msg['From']=sender
    msg['To']=recipient

    return msg


if __name__ == "__main__":
    main()
