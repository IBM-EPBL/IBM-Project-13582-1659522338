import sendgrid

import os

from sendgrid.helpers.mail import Mail, Email, To, Content

sg sendgrid. SendGridAPIClient(api_key-os.environ.get("SENDGRID_API_KEY")) to your verified sender
frome_mail Email("test@example.com") Change
to_email - To("test@example.com") # Change to your recipient
subject - "Sending with Sendorid is Fun" -
content = Content ("text/plain", "and easy to do anywhere, even with Python")
mail-Mail(from_email, to_email, subject, content)

Create PD

•# JSON ready representation at the Mail object

mail json mail.get()

14

#Send an HTTP POST request to /mail/send

response - sg.client.mail.send.post(request body-mail_json)

print(response.status code)

print(response.headers)