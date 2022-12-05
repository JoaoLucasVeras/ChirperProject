import requests
from dotenv import load_dotenv
import os
import math
load_dotenv()


def get_location():
    ip = requests.get('https://api64.ipify.org?format=json').json()
    ip = ip['ip']
    url = f"https://spott.p.rapidapi.com/places/ip/{ip}"

    headers = {
        "X-RapidAPI-Key": os.environ.get('SPOTT_RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "spott.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    return response['name'], response['country']['id']


def get_weather():
    res = {}
    city, country = get_location()

    obj = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}, {country}&appid={os.environ.get('OPENWEATHER_API_KEY')}&units=metric").json()
    res['country'] = country
    res['location']= city
    description = str(obj["weather"][0]["description"]).title()
    res['description'] = description
    res['temp'] = round(obj["main"]["temp"])
    res['feels_like'] = round(obj["main"]["feels_like"])
    res['min_temp'] = round(obj["main"]["temp_min"])
    res['max_temp'] = round(obj["main"]["temp_max"])
    return res


if __name__ == '__main__':
    get_location()
    print(get_weather())