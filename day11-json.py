import json
with open('employees.json', 'r') as file:
    data = json.load(file)
for x in data['employees']:
    if "Kubernetes" in x['skills']:
        print(x['name'])


for yy in data['employees']:
    if yy['age'] > 30:
        print(yy['name'], yy['age'])

import json
movies= {
    "movies": [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
        {"title": "The Matrix", "director": "The Wachowskis", "year": 1999},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014}
    ]
}

with open('movies.json', 'w') as file:
    json.dump(movies, file, indent=4)   