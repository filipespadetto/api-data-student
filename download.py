import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png'

file_name = url.split('/')[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

    with open(file_name, 'wb') as file:
        file.write(response.content)
else:
    print(response.status_code)
    print(response.reason)