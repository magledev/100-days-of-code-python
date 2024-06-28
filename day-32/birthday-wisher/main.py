##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime
import pandas
from random import randint
import smtplib

G_MAIL = "<email_address>"
Y_MAIL = "<email_adress>"
MY_PASSWORD = "<password>"

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_today = data.to_dict()

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    random_letter = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(random_letter) as data:
        contents = data.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    print(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(G_MAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=G_MAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Birthday Greetings\n\n{contents}".encode("utf-8"),
        )
