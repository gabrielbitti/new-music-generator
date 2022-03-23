from fastapi import FastAPI
import requests
# import Weather here!!!!


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
        request_result = requests.get("{url}/weather?lat={lat}&lon={lon}&appid={api_key}".format(url=self.config['base_url'], lat=self.latitude, lon=self.longitude, api_key=self.config['api_key']))
        return request_result.content


app = FastAPI()


@app.get("/")
def root():
    return "New Playlist Generator"


@app.get("/cities/{name}")
def read_city(name: str):
    weather = Weather(city=name, latitude='lattt', longitude='long')
    # TODO get the tempereture of this city
    return {"city_name": weather.current_temperature()}
