#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "test@gmail.com" # your email here
gmail_pwd = "*******"         # your password
#From="amriabdesslem@gmail.com"
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   #msg['From']= sys.argv[1]
   msg['From'] = "sender@gmail.com"
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

#print "xd"
body= From + "This is a email sent with python"
mail("sender@gmail.com",
  "Hello from python!",
   body,
   "missfont.log")


