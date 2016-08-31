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
        resource = '/weather/today/weather/'
        objects = self.get_object_from_request(resource)
        return objects


class TodayPublish(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/weather/today/'
        objects = self.get_object_from_request(resource)
        return objects


class SpecificDayWeather(BaseForMoviesAPIGW, Resource):
    def get(self, date):
        resource = '/weather/%s/weather/' % date
        objects = self.get_object_from_request(resource)
        return objects


class SpecificDayPublish(BaseForMoviesAPIGW, Resource):
    def get(self, date):
        resource = '/weather/%s/' % date
        objects = self.get_object_from_request(resource)
        return objects


def add_resources(api):
    api.add_resource(TodayWeather, '/weather/today/weather/')
    api.add_resource(TodayPublish, '/weather/today/')
    api.add_resource(SpecificDayWeather, '/weather/<string:date>/weather/')
    api.add_resource(SpecificDayPublish, '/weather/<string:date>/')
    return api
