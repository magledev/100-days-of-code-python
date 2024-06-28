# Amazon price tracker using web scraping and notification via email.

import requests
import smtplib
from bs4 import BeautifulSoup

ORIGIN_EMAIL = "<email_address>"
PASSWD = "<password>"

# Take inputs for item and price to track.
item_url = input("What item would you like to track? (Paste the URL): ")
tracked_price = float(input("What is your desired price point?: "))
destination_email = input("What is your email address?: ")

# Scrape Amazon item webpage for relevant info. Providing correct headers to ensure response.
header = {
    "Accept-Language": "en-GB;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 "
    "Safari/537.36",
}
response = requests.get(url=item_url, headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
item_price = float(soup.find(name="span", class_="a-offscreen").getText().strip("£"))
item_title = (
    soup.find(
        name="span", id="productTitle", class_="a-size-large product-title-word-break"
    )
    .getText()
    .strip(" ")
)

# Send email notifying subscriber that their designated price has been met. Include Title, Price and Link to item.
if item_price <= tracked_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        subject = f"Amazon Price Alert for {item_title}!"
        message = f"Your Amazon price alert for {item_title} has been triggered.\n\nThe current price is £{item_price}"
        connection.starttls()
        connection.login(ORIGIN_EMAIL, PASSWD)
        connection.sendmail(
            from_addr=ORIGIN_EMAIL,
            to_addrs=destination_email,
            msg=f"Subject: {subject}\n\n{message}\n\n{item_url}".encode("utf-8"),
        )

print(f"{item_title} - {item_price}")
