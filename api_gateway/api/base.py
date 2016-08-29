import requests
import json


class BaseForAPIGW():
    def __init__(self):
        self.base_url = 'http://localhost:80'
        self.api_key_query = ''

    def response_text_from_request(self, resource):
        request_url = self.base_url + resource + self.api_key_query

        try:
            response = requests.get(request_url)
        except requests.ConnectionError:
            objects = {'error': 'ConnectionError'}
            return objects

        if response.status_code != 200:
            objects = {'error': 'Statuscode : %s' % response.status_code}
            return objects

        text = response.text
        objects = json.loads(text)

        return objects
