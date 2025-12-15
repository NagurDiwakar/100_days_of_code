import requests

response = requests.get(url="https://api.kanye.rest/")

response_code = response.status_code

data = response.json()

actual_quote = data["quote"]
print(response_code)
print(actual_quote)