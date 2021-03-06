from typing import Optional
from fastapi import FastAPI, HTTPException
from modules.open_weather import OpenWeather

app = FastAPI()


@app.get("/")
def index():
    return 'New Playlist Generator'


@app.get("/cities/playlists")
def read_cities_playlists(city: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None):
    try:
        open_weather = OpenWeather(city, latitude, longitude)
        temperature_in_celcius = open_weather.get_current_temperature_in_celcius()
        spotify_playlists = open_weather.get_playlists_for_current_temperature()
    except:
        raise HTTPException(status_code=400, detail='City not found')

    response = {
        'city_name': open_weather.city_name,
        'temperature_in_celcius': temperature_in_celcius,
        'spotify_playlists': spotify_playlists,
    }

    return response


@app.get("/cities/tracks")
def read_cities_tracks(city: Optional[str] = None, latitude: Optional[float] = None, longitude: Optional[float] = None):
    open_weather = OpenWeather(city, latitude, longitude)
    temperature_in_celcius = open_weather.get_current_temperature_in_celcius()
    spotify_tracks = open_weather.get_tracks_for_current_temperature()

    try:
        open_weather = OpenWeather(city, latitude, longitude)
        temperature_in_celcius = open_weather.get_current_temperature_in_celcius()
        spotify_tracks = open_weather.get_tracks_for_current_temperature()
    except:
        raise HTTPException(status_code=400, detail='City not found')

    response = {
        'city_name': open_weather.city_name,
        'temperature_in_celcius': temperature_in_celcius,
        'spotify_tracks': spotify_tracks,
    }

    return response
