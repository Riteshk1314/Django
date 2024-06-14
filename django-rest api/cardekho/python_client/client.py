import requests
endpoints="http://127.0.0.1:8000/car/list"

getresposnse=requests.get(endpoints)
print(getresposnse.json())
print(getresposnse.status_code)