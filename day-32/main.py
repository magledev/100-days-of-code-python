import smtplib
import datetime
from random import choice
from email.mime.text import MIMEText

G_MAIL = "<email_address>"
Y_MAIL = "<email_address>"
MY_PASSWORD = "<password>"

now = datetime.datetime.now()
current_day = now.strftime("%A")

if current_day == "Friday":
    with open("quotes.txt", "r") as data:
        quotes_list = data.readlines()
        quote = choice(quotes_list)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(G_MAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=G_MAIL,
            to_addrs=Y_MAIL,
            msg=f"Subject:Daily motivational quote\n\n{quote}".encode("utf-8"),
        )
