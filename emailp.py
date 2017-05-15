"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib

gmail_user = 'guillaume.ronan.thomas@gmail.com'
gmail_password = input('Password ?\n')
sent_from = gmail_user
to = ["guillaumethomas@outlook.com"]

subject ="Email sent from python script"
body = "corps de texte"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
except:
    print('Something went wrong...')

