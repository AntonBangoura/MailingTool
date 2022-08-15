import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.ehlo()


server.login('XXXX', 'XXXXX')

msg = MIMEMultipart()
msg["From"] = "XXXX"
msg['To'] = 'XXXX'
msg['Subject'] = 'Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'caesar.jpg'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}') 
msg.attach(p)

text = msg.as_string()
server.sendmail('XXXX', 'XXXXX', text)
