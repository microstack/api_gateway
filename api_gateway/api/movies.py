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
        objects = self.get_object_from_request(resource)
        return objects


class MoviesLatest(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/latest/'
        objects = self.get_object_from_request(resource)
        return objects


class MoviesHighGrade(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/grade/'
        objects = self.get_object_from_request(resource)
        return objects


class GenreList(BaseForMoviesAPIGW, Resource):
    def get(self):
        resource = '/movies/genres/'
        objects = self.get_object_from_request(resource)
        return objects

   
class GenreMovieList(BaseForMoviesAPIGW, Resource):
    def get(self, name):
        resource = '/movies/genres/%s/' % name
        objects = self.get_object_from_request(resource)
        return objects


def add_resources(api):
    api.add_resource(MovieList, '/movies/')
    api.add_resource(MoviesLatest, '/movies/latest/')
    api.add_resource(MoviesHighGrade, '/movies/grade/')
    api.add_resource(GenreList, '/movies/genres/')
    api.add_resource(GenreMovieList, '/movies/genres/<string:name>/')
    
    return api
