from fastapi import FastAPI
import requests
import json
# TODO import Weather here!!!!


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

        return request_result.content


app = FastAPI()


@app.get("/")
def root():
    return "New Playlist Generator"


@app.get("/cities/{name}")
def read_city(name: str):
    weather = Weather(city=name, latitude='', longitude='')
    current_temperature = weather.current_temperature()

    my_json = current_temperature.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    temperature_in_celcius = float(data['main']['temp']) - 273.15
    temperature_in_celcius = "{0:.0f}".format(round(temperature_in_celcius, 2))

    response = {
        'city': name.capitalize(),
        'temperature_in_celcius': temperature_in_celcius,
    }

    return response
