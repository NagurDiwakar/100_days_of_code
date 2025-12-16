import datetime as dt
import pandas as pd
import random
import smtplib

today_time = dt.datetime.now()
today_month = today_time.month
today_day = today_time.day

today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_email@gmail.com", password="your_password")
        connection.sendmail(
            from_addr="your_email@gmail.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )