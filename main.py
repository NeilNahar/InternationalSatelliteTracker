import requests
import smtplib
import datetime as dt
import math

MY_LATITUDE=32.7251689
MY_LONGITUDE=-97.1202917

my_email="aj0040976@gmail.com"
password="uvqyhozbxiumjibq"
recieving_email="aj311840@gmail.com"

currenttime=dt.datetime.now()
current_hour=currenttime.hour

response1=requests.get("http://api.open-notify.org/iss-now.json")
response1.raise_for_status()

cordinates=response1.json()["iss_position"]
latitude=round(float(cordinates["latitude"]),1)
longitude=round(float(cordinates["longitude"]),1)

parameter={"lat":MY_LATITUDE,"lng":MY_LONGITUDE,"formatted":0}
response2=requests.get(url=" https://api.sunrise-sunset.org/json",params=parameter)
response2.raise_for_status()

data=response2.json()
sunrise=data["results"]["sunrise"][11:18].split(":")
sunset=data["results"]["sunset"][11:18].split(":")

if int(sunrise[0])>current_hour or current_hour>int(sunset[0]):
    if math.floor(latitude)-1<MY_LATITUDE and math.ceil(latitude)+1>MY_LATITUDE and math.floor(longitude)-1<MY_LONGITUDE and math.ceil(longitude)+1>MY_LONGITUDE:
        print("International SatelighT is Above")
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=recieving_email,msg="subject:Satelight\n\nSatelight is above you")
        connection.close()
    else:
        print("International SatelighT is not Above")
else:
    print("Light is not dark to see the International Satelight")