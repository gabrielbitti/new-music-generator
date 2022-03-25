from fastapi import FastAPI, HTTPException
from weather.open_weather import OpenWeather

app = FastAPI()


@app.get("/")
def index():
    return 'New Playlist Generator'


@app.get("/cities/playlists")
def read_cities_playlists(city: str = '', latitude: str = '', longitude=''):
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
def read_cities_tracks(city: str = '', latitude: str = '', longitude=''):
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
