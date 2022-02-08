import requests
from pprint import pprint

_print = print
print = pprint

url = "http://127.0.0.1:3001/users"

user_data = {
    "nome": "Filipe Spadetto",
    "password": "123456",
    "email": "filipe@email.com"
}

response = requests.post(url, user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print("Status code: ", response.status_code)
    print("Reason: ", response.reason)
    print("Reason: ", response.text)
    print("JSON: ", response.json())
else:
    print("Status code: ", response.status_code)
    print("Reason: ", response.reason)
    print("Reason: ", response.text)
    print("JSON: ", response.json())