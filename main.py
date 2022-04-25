import requests
import smtplib

MY_LAT = -22.289181
MY_LNG = -42.534561

PARAMS = {
    "lat": MY_LAT,
    "lng": MY_LNG
}
response = requests.get("https://api.sunrise-sunset.org/json",params=PARAMS)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

text = f"Subject:BOM DIA!\n\nHoje o dia nasceu as {sunrise} e vai se por as {sunset}\n E Nois!"

email = "joaobuzato@gmail.com"
password = "fcFdrRQ9v6@$"
login = "hojeosolnasceas@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=login, password=password)
    connection.sendmail(from_addr=login, to_addrs=email, msg=text)
