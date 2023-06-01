import smtplib
import sqlite3
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import pandas as pd
import schedule
from pretty_html_table import build_table

import creds


def sendEmail():
    con = sqlite3.connect("db.sqlite3")
    df = pd.read_sql_query("SELECT * FROM inventory_stock", con)
    con.close()
    table = build_table(df[(df['quantity'] < 100)], 'blue_light')

    try:
        message = MIMEMultipart()
        message['Subject'] = 'LOW STOCKS ALERT!!!'

        body_content = table
        message.attach(MIMEText(body_content, "html"))
        msg_body = message.as_string()
        print("Sending Alert!")
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(creds.MY_EMAIL, creds.PASSWORD)
        s.sendmail(from_addr=creds.MY_EMAIL, to_addrs=["atharvakgaikwad11@gmail.com", "202101006.siddharthbds@student.xavier.ac.in","bansid2963@gmail.com"],
                   msg=msg_body)
        s.quit()
        print("E-mail Sent!!")
    except Exception as e:
        raise Exception("Errors occurred while sending email", e)


def sendDailyMail():
    schedule.every().day.at("05:30").do(sendEmail)

    while True:
        schedule.run_pending()
        time.sleep(1)


sendEmail()
# sendDailyMail()
