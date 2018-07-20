import smtplib

def send_mail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        server.starttls()
        server.login("Email", "Password")  # your email and password here
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("Email", "client's email", message)
        server.quit()
        print("sent")
    except:
        print("failed")


send_mail('LOL', 'trolling you')

# full version of the email sending system
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# user = 'Email'  # your email
# password = 'Password'  # your password
# client = 'tasmiyah.t07@gmail.com'  # clients password
#
# subject = 'subject'
#
# msg = MIMEMultipart()
# msg['From'] = user
# msg['To'] = client
# msg['Subject'] = subject
#
# body = 'Lol'
# msg.attach(MIMEText(body, 'plain'))
#
# filename = 'filename'  # filename or the path
# attachment = open(filename, 'rb')
#
# part = MIMEBase('application','octet-stream')
# part.set_payload(attachment).read()
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= " + filename)
#
# msg.attach(part)
# text = msg.as_string()
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(user, password)
#
#
# server.sendmail(user, client, text)
# server.quit()
