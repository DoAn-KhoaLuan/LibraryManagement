import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From']="shinichi24567@gmail.com"
msg['To']="1751012015hai@ou.edu.vn"
msg.set_content("how do you think about me Hai dep trai? ")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("shinichi24567@gmail.com", "shinichi24567123")
    smtp.send_message(msg)
