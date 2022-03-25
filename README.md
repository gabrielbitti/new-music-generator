# New Music Generator
Get Spotify playlists or tracks according to your location (city name or longitude/latitude).

## How does it work?
You can navigate to 127.0.0.1/docs to read the docs and test my routes. I did two GET requests: one for returning *playlists*, other returning *tracks*.

To get music information, I used [Spotify Web API](https://developer.spotify.com/documentation/web-api/) and to get current weather information, I used [OpenWeather API](https://openweathermap.org/current/).

## Installation

### Built Docker project image
Run `docker build -t <image_name> .`

### Run project
Run `docker run -p 8000:8000 --name <container_name> <image_name>`

### See it running
Go to `127.0.0.1:8000` and you can make the requests.
