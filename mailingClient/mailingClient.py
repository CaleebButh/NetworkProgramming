#library to use smtp secure mail transfer protocol
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#connects to the gmail smtp server over port 25 which is the standard port for smtp
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

with open('password.txt', 'r') as file:
    password = file.read()

#login to the server using the email and password from the file
server.login('ungabungward@gmail.com', password)

#creates a MIMEMultipart message object and attaches the message content to it.
msg = MIMEMultipart()
msg['From'] = 'Dr. Bungward'
msg['To'] = 'caleb.buth@gmail.com'
msg['Subject'] = 'Is this thing ON??'
with open('message.txt', 'r') as file:
    message = file.read()
msg.attach(MIMEText(message, 'plain'))

#Reads the image file and sets payload to file contents.
filename = 'flower.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
#encodes the information into an image and attaches it to the message
encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)

#converts the msg to string format and sends message via our smtp connection.
text = msg.as_string()
server.sendmail("ungabungward@gmail.com", "caleb.buth@gmail.com", text)
print("Message sent!")