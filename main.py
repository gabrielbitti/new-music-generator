from re import A
from fastapi import FastAPI
import requests
import json
import base64
from requests.auth import HTTPBasicAuth
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

    def get_current_temperature(self):
        request_result = requests.get("{url}/weather?q={city}&appid={api_key}".format(
            url=self.config['base_url'], city=self.city_name, api_key=self.config['api_key']))

        return request_result.content
        # return request_result.json() # TODO test

    def get_playlist_for_current_temperature(self, temperature):
        temperature = self.get_current_temperature(temperature)
        # TODO buscar da classe spotify


class Spotify:
    config = {
        'client_id': 'da23a865663b4d6c8d2f3626178efb5f',
        'client_secret': '120db78513cf451984b7bef16bd6e873',
        'base_url': 'https://api.spotify.com/v1',
    }

    def __init__(self):
        pass

    def client_credentials_authorization(self):
        payload = {
            'grant_type': 'client_credentials',
        }

        # base64encoded = base64.b64encode(self.config['client_id'] + ':' + self.config['client_secret'])
        base64encoded = base64.b64encode('da23a865663b4d6c8d2f3626178efb5f:120db78513cf451984b7bef16bd6e873'.encode())

        headers = {
            'Authorization': 'Basic {base64encoded}'.format(base64encoded=base64encoded.decode()),
            # 'Authorization': HTTPBasicAuth(self.config['client_id'], self.config['client_secret']),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.post(url='https://accounts.spotify.com/api/token', data=payload, headers=headers)
        return response.json()

    def get_from_category_slug(self, category):
        authorization = self.client_credentials_authorization()
        access_token = authorization['access_token']

        headers = {
            'Authorization': f'Bearer {access_token}',
        }

        url = "{url}/browse/categories/{category_id}/playlists?client_id={key}".format(
           url=self.config['base_url'], category_id=category, key=self.config['client_id'])
        request_result = requests.get(url=url, headers=headers)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(request_result.json())

        return request_result.json()


app = FastAPI()


@app.get("/")
def root():
    return "New Playlist Generator"


@app.get("/cities/{name}")
def read_city(name: str):
    weather = Weather(city=name, latitude='', longitude='')
    current_temperature = weather.get_current_temperature()

    my_json = current_temperature.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    temperature_in_celcius = float(data['main']['temp']) - 273.15
    temperature_in_celcius = "{0:.0f}".format(round(temperature_in_celcius, 2))

    spotify = Spotify()

    response = {
        'city': name.capitalize(),
        'temperature_in_celcius': temperature_in_celcius,
        'spotify_playlist': spotify.get_from_category_slug('party'),
    }

    return response
