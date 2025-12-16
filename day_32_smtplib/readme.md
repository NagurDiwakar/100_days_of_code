smtplib is library in Python used to send emails using the Simple Mail Transfer Protocol (SMTP). It defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

smtp uses the port 25 by default for non-encrypted communication and port 587 for encrypted communication using STARTTLS. For secure communication over SSL/TLS, port 465 is commonly used.

Here is a simple example of how to use smtplib to send an email:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Set up the server
smtp_server = "smtp.example.com"
smtp_port = 587
username = "random@example.com"
password = "your_password"
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
server.login(username, password)
# Create the email
from_email = "random@example.com"
to_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent using smtplib in Python."

message = MIMEMultipart()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# Send the email
server.sendmail(from_email, to_email, message.as_string())
server.quit()