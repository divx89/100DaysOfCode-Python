import datetime as dt
import smtplib
import pandas

today = dt.datetime.today()
day_of_week = today.weekday()

if day_of_week == 2:
    print("Okay to send")
    quote = pandas.read_csv("quotes.txt").sample().to_string(index=False, header=None)
    with smtplib.SMTP(host="smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="divx93415@yahoo.com", password="")
        connection.sendmail(from_addr="divx93415@yahoo.com",
                            to_addrs="divx93415@gmail.com",
                            msg=f"Subject:Today's motivational quotation!\n\n{quote}")
