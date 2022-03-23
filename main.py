from fastapi import FastAPI
import requests
import json
# TODO import Weather here!!!!


"""
Call current weather data

API KEY: b77e07f479efe92156376a8b07640ced
https://api.openweathermap.org/data/2.5
"""


class Weather():
    config = {
        'api_key': 'b77e07f479efe92156376a8b07640ced',
        'base_url': 'https://api.openweathermap.org/data/2.5',
    }

    def __init__(self, city, latitude, longitude):
        self.city_name = city
        self.latitude = latitude
        self.longitude = longitude

    def current_temperature(self):
        request_result = requests.get("{url}/weather?q={city}&appid={api_key}".format(
            url=self.config['base_url'], city=self.city_name, api_key=self.config['api_key']))
        request_content = request_result.content
        #request_content.temperature_in_celcius = request_content.main.temp #- 237.15

        return request_content


app = FastAPI()


@app.get("/")
def root():
    return "New Playlist Generator"


@app.get("/cities/{name}")
def read_city(name: str):
    weather = Weather(city=name, latitude='', longitude='')
    current_temperature = weather.current_temperature()
    tempereture = current_temperature

    my_json = current_temperature.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    # s = json.dumps(data, indent=4, sort_keys=True)
    temperature_in_celcius = int(data['main']['temp']) - 237

    return {'temperature': temperature_in_celcius}
