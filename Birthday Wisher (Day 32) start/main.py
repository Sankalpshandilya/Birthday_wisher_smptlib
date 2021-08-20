import smtplib
import datetime as dt
import random
mymail = "sankalpshandilyanit@gmail.com"
password ="Sankalpnit"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open ("quotes.txt") as quotes_n_thoughts:
        allquote = quotes_n_thoughts.readlines()
        quotes = random.choice(allquote)

        print(quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(mymail, password)
            connection.sendmail(from_addr=mymail,
                                to_addrs="Shandilya.sankalp01@gmail.com",
                                msg=f"Subject:Quote of the day\n\nHello Sankalp \nI hope you are doing well \n{quotes}")
