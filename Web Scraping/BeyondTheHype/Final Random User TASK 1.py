import requests
import csv

url = 'https://randomuser.me/'

params = {
    'results': 100,
    'gender': 'male'
}

r = requests.get(url)
print(r)

data = r.json()
users = data.get('results', [])

csv_file_path = 'male_users.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Email', 'DOB', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for user in users:
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        dob = user['dob']['date']
        phone = user['phone']

        writer.writerow({'Name': name, 'Email': email, 'DOB': dob, 'Phone': phone})
print(f"Data exported to {csv_file_path}")