# (c) AtomMail 2022. All rights reserved.
# This is a copy of Version 1.0.0
import time
import getpass
import smtplib


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\nMIME-Version: 1.0\nContent-Type: text/html\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")



print("""

    ___   __                  __  ___      _ __
   /   | / /_____  ____ ___  /  |/  /___ _(_) /
  / /| |/ __/ __ \/ __ `__ \/ /|_/ / __ `/ / / 
 / ___ / /_/ /_/ / / / / / / /  / / /_/ / / /  
/_/  |_\__/\____/_/ /_/ /_/_/  /_/\__,_/_/_/   
                                               

""")
print("Hello! Welcome to AtomMail. Please make sure you have a gmail account.")
time.sleep(1)
print("Then please enable 2-Step Verification here if you haven't already: https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome")
time.sleep(1)
print("Then set a App Password if you haven't yet. Set it here: https://myaccount.google.com/u/0/apppasswords.")
time.sleep(1)
print("Then set the app name to other and name it AtomMail and genereate. Remember that app password - it is the password to login to AtomMail.")
time.sleep(1)
print()
print("LOGIN")
print()
username = input("Email: ")
password = getpass.getpass()
print("Logging in... Please wait.")
time.sleep(1)
print()
print()
print()
print()
while True:
    person = input("To: ")
    sub = input("Subject: ")
    text = input("Body (use <br> for line breaks - html notation): ")
    send_email(username, password, person, sub, text)
    print()