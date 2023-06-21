import requests

response = requests.get("https://geo.api.gouv.fr/communes/59115")
result = response.json()

print(type(result))
for column,value in result.items():
    print(f"{column} : {value}")