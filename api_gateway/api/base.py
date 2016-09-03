import requests
import json


class BaseForAPIGW():
    def __init__(self):
        self.base_url = 'http://localhost:80'
        self.api_key_query = ''

    def get_object_from_request(self, resource):
        '''
        To escape the doubled jsonified text,
        it converts the response text to the object.
        '''

        def _get_request_url():
            return self.base_url + resource + self.api_key_query

        text = ''

        try:
            response = requests.get(_get_request_url())
        except requests.ConnectionError:
            text = '{"status": 500, "exception": "ConnectionError"}'
        else:
            text = response.text

        objects = json.loads(text)

        if isinstance(objects, dict):
            server_error_msg = objects.get("message")
            if server_error_msg == "Internal Server Error":
                objects = {"status": 500, "exception": server_error_msg}

        return objects
