import smtplib

yahoo_login = "divx93415@yahoo.com"
yahoo_pass = ""
yahoo_host = "smtp.mail.yahoo.com"

gmail_login = "divx93415@gmail.com"
gmail_pass = ""
gmail_host = "smtp.gmail.com"

with smtplib.SMTP(host=gmail_host) as connection:
    connection.starttls()
    connection.login(user=gmail_login, password=gmail_pass)
    connection.sendmail(from_addr=gmail_login,
                        to_addrs=yahoo_login,
                        msg="Subject:Hello\n\nThis is a test email message")

with smtplib.SMTP(host=yahoo_host) as connection:
    connection.starttls()
    connection.login(user=yahoo_login, password=yahoo_pass)
    connection.sendmail(from_addr=yahoo_login,
                        to_addrs=gmail_login,
                        msg="Subject:Test Email from Code\n\nThis is a test email written through code.")
