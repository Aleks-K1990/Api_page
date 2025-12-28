import requests
from urllib3.util import url

def request_get(url):
    response = requests.get(url)
    json_content = response.json()
    for item in json_content['data']:
        print(item['attributes']['name'])

n = 1
command_1 = input("Нажми 1, чтобы показать первые 5 пород: ").lower().strip()
if command_1 == '1':
    request_get("https://dogapi.dog/api/v2/breeds?page%5Bsize%5D=5")

command_2 = input("Нажми 1, чтобы показать следующие 5 пород: ").lower().strip()
if command_2 == '1':
    n +=1
    request_get(f'https://dogapi.dog/api/v2/breeds?page[number]={n}&page[size]=5')

t = True
while t:

    command_3 = input("Нажми 1, чтобы показать следующие 5 пород;\n"
                      "Нажми 2, чтобы показать предыдущие 5 пород: ").lower().strip()
    if command_3 == '1':
        n +=1
        request_get(f'https://dogapi.dog/api/v2/breeds?page[number]={n}&page[size]=5')

    elif command_3 == '2':
        n -=1
        request_get(f'https://dogapi.dog/api/v2/breeds?page[number]={n}&page[size]=5')
    else:
        print("Вы ввели неверную команду.")