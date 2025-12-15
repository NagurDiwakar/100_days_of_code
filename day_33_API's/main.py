import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
print(response.status_code)

# instead of writing each error status we can use error status exception

# https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions

# to check the long and lati u can use this https://www.latlong.net/Show-Latitude-Longitude.html

response.raise_for_status()

data = response.json()

longitude  = data["iss_position"]["longitude"]
latitude  = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

