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

    def get_current_temperature(self):
        request_result = requests.get("{url}/weather?q={city}&appid={api_key}".format(
            url=self.config['base_url'], city=self.city_name, api_key=self.config['api_key']))

        return request_result.json()

    def get_playlist_for_current_temperature(self):
        temperature = self.get_current_temperature()
        temperature_in_celcius = float(temperature['main']['temp']) - 273.15

        spotify = Spotify()
        playlists_category = spotify.get_category_by_current_temperature(
            temperature_in_celcius)

        return spotify.get_playlists_from_category_slug(playlists_category)
