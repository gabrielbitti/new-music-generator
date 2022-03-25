import base64
import requests


class Spotify:
    config = {
        'client_id': 'da23a865663b4d6c8d2f3626178efb5f',
        'client_secret': '120db78513cf451984b7bef16bd6e873',
        'base_url': 'https://api.spotify.com/v1',
    }

    def client_credentials_authorization(self):
        payload = {
            'grant_type': 'client_credentials',
        }

        to_encode = self.config['client_id'] + \
            ':' + self.config['client_secret']
        base64encoded = base64.b64encode(to_encode.encode())
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {base64encoded}'.format(base64encoded=base64encoded.decode()),
        }

        response = requests.post(
            url='https://accounts.spotify.com/api/token', data=payload, headers=headers)

        return response.json()

    def get_playlists_from_category_slug(self, category):
        authorization = self.client_credentials_authorization()
        access_token = authorization['access_token']
        headers = {
            'Authorization': f'Bearer {access_token}',
        }

        url = "{url}/browse/categories/{category_id}/playlists?client_id={key}".format(
            url=self.config['base_url'], category_id=category, key=self.config['client_id'])

        request_result = requests.get(url=url, headers=headers)
        return request_result.json()

    def get_category_by_current_temperature(self, temperature):
        if temperature > 30:
            return 'party'
        if temperature >= 15 and temperature <= 30:
            return 'pop'
        if temperature >= 10 and temperature <= 14:
            return 'rock'
        if temperature < 10:
            return 'classic music'
