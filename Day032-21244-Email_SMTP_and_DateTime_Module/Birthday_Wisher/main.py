##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas
import datetime as dt

files = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

today = dt.date.today()
data_frame = pandas.read_csv("birthdays.csv")

for index, row in data_frame.iterrows():
    row_date = dt.date(int(row['year']), int(row['month']), int(row['day']))

    if row_date.month == today.month and row_date.day == today.day:
        with open(random.choice(files)) as file:
            message = file.read().replace("[NAME]", row['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="divx93415@gmail.com", password="")
            connection.sendmail(from_addr="divx93415@gmail.com",
                                to_addrs=row['email'],
                                msg=f"Subject:Happy Birthday!\n\n{message}")
