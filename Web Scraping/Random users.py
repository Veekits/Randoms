import requests
import pandas as pd

url = 'https://randomuser.me/api/'

params = {
    'results': 100,
    'gender': 'male'
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    users = data.get('results', [])
    for index, user in enumerate(users, start=1):
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        dob = user['dob']['date']
        phone = user['phone']

        print(f"{index}. Name: {name}, Email: {email}, DOB: {dob}, Phone: {phone}")

else:
    print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
