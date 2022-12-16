import requests


def response(url):
    ip_url = url
    res = requests.get(ip_url)
    info = res.json()
    return info


data = response('https://api.ipify.org?format=json')

ip = data.get('ip')

data = response(f'https://ipapi.co/{ip}/json/')
main_ip = data.get('ip')
city = data.get('city')
country_name = data.get('country_name')
sentence = f"{main_ip} is from {city} which is in {country_name}"

print(sentence)
