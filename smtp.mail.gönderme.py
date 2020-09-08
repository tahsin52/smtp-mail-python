import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "mail"

mesaj["To"] = "mail"

mesaj["Subject"] = "Smtp Mail Gönderme."

yazi = """

SMTP ile mail gönderiyorum..

Tahsin Can Ülgen

"""
mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("mail@hotmail.com","password")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail Başarıyla Gönderildi..")

    mail.close()

except:
    sys.stderr.write("Bir Sorun Oluştu")
    sys.stderr.flush()
