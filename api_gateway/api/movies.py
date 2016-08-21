# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api.base import BaseForAPIGW
from api_gateway.settings import BACKEND_MOVIES_BASE_URL


class BaseForMoviesAPIGW(BaseForAPIGW):
    def __init__(self):
        self.base_url = BACKEND_MOVIES_BASE_URL
        self.api_key_query = ''


class MovieList(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/'
        objects = self.response_text_from_request(resource)
        return text


class MoviesLatest(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/latest/'
        objects = self.response_text_from_request(resource)
        return objects


class MoviesHighGrade(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/grade/'
        objects = self.response_text_from_request(resource)
        return objects


def add_resources(api):
    api.add_resource(MovieList, '/movies/')
    api.add_resource(MoviesLatest, '/movies/latest/')
    api.add_resource(MoviesHighGrade, '/movies/grade/')
    
    return api
