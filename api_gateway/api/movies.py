# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api_gateway.settings import MOVIES_BASE_URL


class BaseForAPIGW():
    def __init__(self):
        self.base_url = MOVIES_BASE_URL

    def response_text_from_request(self, resource):
        response = requests.get(self.base_url + resource)
        text = response.text
        return text

class MovieList(BaseForAPIGW, Resource):
    def get(self):
        resource = '/movies/'
        return 'wow'


def add_resources(api):
    api.add_resource(MovieList, '/movies/')
    return api
