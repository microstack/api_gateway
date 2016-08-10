import requests


class BaseForAPIGW():
    def __init__(self):
        self.base_url = ''

    def response_text_from_request(self, resource):
        response = requests.get(self.base_url + resource)
        text = response.text
        return text
