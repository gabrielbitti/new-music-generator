from fastapi import HTTPException
from sound.spotify import Spotify
import requests


class OpenWeather():
    config = {
        'api_key': 'b77e07f479efe92156376a8b07640ced',
        'base_url': 'https://api.openweathermap.org/data/2.5',
    }

    def __init__(self, city, latitude, longitude):
        self.city_name = city
        self.latitude = latitude
        self.longitude = longitude

    def get_search_term_by_current_temperature(self, temperature):
        temperature = float(temperature)
        if temperature > 30:
            return 'party'
        if temperature >= 15 and temperature <= 30:
            return 'pop'
        if temperature >= 10 and temperature <= 14:
            return 'rock'
        if temperature < 10:
            return 'classic music'

    def get_weather_data(self):
        base_url = "{url}/weather".format(url=self.config['base_url'])

        if self.city_name != None:
            params = {
                'q': self.city_name,
                'appid': self.config['api_key'],
            }

            response = requests.get(url=base_url, params=params)
            return response.json()
        
        if self.latitude != None and self.longitude != None:
            params = {
                'lat': self.latitude,
                'lon': self.longitude,
                'appid': self.config['api_key'],
            }

            response = requests.get(url=base_url, params=params)
            return response.json()
        
        return False

    def get_current_temperature_in_celcius(self):
        try:
            weather_data = self.get_weather_data()
            temperature_in_celcius = float(weather_data['main']['temp']) - 273.15
            return "{0:.0f}".format(round(temperature_in_celcius, 2))
        except:
            raise HTTPException(status_code=400, detail='City informations is invalid')

    def get_playlists_for_current_temperature(self):
        temperature_in_celcius = self.get_current_temperature_in_celcius()
        to_search = self.get_search_term_by_current_temperature(
            temperature_in_celcius)

        items = []

        spotify = Spotify()
        search_result = spotify.search(to_search, 'playlist')
        for item in search_result['playlists']['items']:
            items.append({
                'name': item['name'],
                'url': item['external_urls']['spotify'],
            })

        return items

    def get_tracks_for_current_temperature(self):
        temperature_in_celcius = self.get_current_temperature_in_celcius()
        to_search = self.get_search_term_by_current_temperature(
            temperature_in_celcius)

        items = []

        spotify = Spotify()
        search_result = spotify.search(to_search, 'track')
        for item in search_result['tracks']['items']:
            artists = []
            for artist in item['album']['artists']:
                artists.append(artist['name'])

            items.append({
                'name': item['name'],
                'artist': ', '.join(artists),
                'url': item['external_urls']['spotify'],
            })

        return items
