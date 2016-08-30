# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api.base import BaseForAPIGW
from api_gateway.settings import BACKEND_WEATHER_BASE_URL


class BaseForMoviesAPIGW(BaseForAPIGW):
    def __init__(self):
        self.base_url = BACKEND_WEATHER_BASE_URL
        self.api_key_query = ''


class TodayWeather(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/weather/today/'
        objects = self.response_text_from_request(resource)
        return objects


def add_resources(api):
    api.add_resource(TodayWeather, '/weather/today/')
    
    return api
