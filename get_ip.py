import requests
import json

# getting ip addres
def get_ip():
    r = requests.get('https://api.ipify.org/')
    rct = r.text
    return rct

print(get_ip())  # printing ip adress