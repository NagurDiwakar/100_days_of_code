import requests
from datetime import datetime
Latitude = "163.07"
Longitude = "-0.1231"


parameters = {
    "lat" : Latitude,
    "lng" : Longitude,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters )

data = response.json()
sun_rise  = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now =  datetime.now()
#print(time_now)
#print(data)
print(sun_rise)

response.raise_for_status()
# to split the string by sunrise and sunset time


