import requests
from pprint import pprint
from get_token2 import token

_print = print
print = pprint

url = "http://127.0.0.1:3001/alunos"

headers = {
    'Authorization': token
}

student_data = {
    "nome": "Luana",
    "sobrenome": "Luna",
    "email": "luana@email.com",
    "idade": "25",
    "peso": "60.0",
    "altura": "1.70"
}

response = requests.post(url, student_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)