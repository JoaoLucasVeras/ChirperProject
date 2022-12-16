import requests
import os
from flask import session
def get_location():
    
    response = requests.get(f"https://api.maptiler.com/geolocation/ip.json?key={os.environ.get('MAP_KEY')}").json()
    return response['city'], response['country_code']


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
