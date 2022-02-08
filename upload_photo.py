import requests
from pprint import pprint
from get_token2 import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

_print = print
print = pprint

mimetypes = MimeTypes()
file_name = "py_logo.png"
mimetype_file = mimetypes.guess_type(file_name)[0]

multipart = MultipartEncoder(fields={
    "aluno_id": "2",
    "foto": (file_name, open(file_name, 'rb'), mimetype_file) 
})


url = "http://127.0.0.1:3001/fotos"

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url, headers=headers, data=multipart)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)