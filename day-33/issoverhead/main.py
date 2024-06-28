from datetime import datetime
import requests
import smtplib
import time

MY_LAT = 50.375458
MY_LONG = -4.142657
G_MAIL = "<email_address>"
PASSWD = "<password>"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    # Your position is within +5 or -5 degrees of the ISS position.
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


# If it is dark.
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# Send email to tell me to look up.
def notify_observer():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(G_MAIL, PASSWD)
        connection.sendmail(
            from_addr=G_MAIL,
            to_addrs=G_MAIL,
            msg="Subject: ISS Notifier\n\nThe ISS is overhead and it is dark, go outside and look up!".encode(
                "utf-8"
            ),
        )


# Run the code every 120 seconds.
while True:
    time.sleep(120)
    if iss_overhead() and is_night():
        notify_observer()
