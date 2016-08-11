import requests


class BaseForAPIGW():
    def __init__(self):
        self.base_url = 'http://localhost:80'
        self.api_key_query = ''

    def response_text_from_request(self, resource):
        request_url = self.base_url + resource + self.api_key_query
        response = requests.get(request_url)
        text = response.text
        return text
