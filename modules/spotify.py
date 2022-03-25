import base64
import requests


class Spotify:
    config = {
        'client_id': 'da23a865663b4d6c8d2f3626178efb5f',
        'client_secret': '120db78513cf451984b7bef16bd6e873',
        'base_url': 'https://api.spotify.com/v1',
    }

    def get_access_token(self):
        authorization = self.client_credentials_authorization()
        return authorization['access_token']

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

    def search(self, arguments, type):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.get_access_token()}'
        }

        params = {
            'q': arguments,
            'type': type,
        }

        url = "{url}/search".format(url=self.config['base_url'])

        response = requests.get(url=url, headers=headers, params=params)
        return response.json()
