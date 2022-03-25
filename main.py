from fastapi import FastAPI
from weather.open_weather import OpenWeather

app = FastAPI()


@app.get("/")
def root():
    return "New Playlist Generator to SAFE Labs :D"


@app.get("/cities/{name}")
def read_city(name: str):
    open_weather = OpenWeather(city=name, latitude='', longitude='')
    current_temperature = open_weather.get_current_temperature()

    temperature_in_celcius = float(
        current_temperature['main']['temp']) - 273.15

    temperature_in_celcius = "{0:.0f}".format(round(temperature_in_celcius, 2))

    playlists = open_weather.get_playlist_for_current_temperature()

    response = {
        'city': name.capitalize(),
        'temperature_in_celcius': temperature_in_celcius,
        'spotify_playlist': playlists,
    }

    return response
