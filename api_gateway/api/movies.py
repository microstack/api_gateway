# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api.base import BaseForAPIGW
from api_gateway.settings import MOVIES_BASE_URL


class BaseForMoviesAPIGW(BaseForAPIGW):
    def __init__(self):
        self.base_url = MOVIES_BASE_URL


class MovieList(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/'
        text = self.response_text_from_request(resource)
        return text


def add_resources(api):
    api.add_resource(MovieList, '/movies/')
    return api
