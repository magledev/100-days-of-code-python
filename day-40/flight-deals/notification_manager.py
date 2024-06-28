from twilio.rest import Client

TWILIO_SID = "<twilio_sid>"
TWILIO_AUTH_TOKEN = "<twilio_auth_token>"
TWILIO_VIRT_NO = "<twilio_virt_no>"
TWILIO_VERI_NO = "<twilio_veri_no"


class NotificationManger:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRT_NO,
            to=TWILIO_VERI_NO,
        )
        print(message.sid)

    def send_emails(self, emails, message, link):
        pass
