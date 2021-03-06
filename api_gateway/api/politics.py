# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api.base import BaseForAPIGW
from api_gateway.settings import BACKEND_POLITICS_BASE_URL, \
    BACKEND_POLITICS_API_KEY_QUERY


class BaseForPoliticsAPIGW(BaseForAPIGW):
    def __init__(self):
        self.base_url = BACKEND_POLITICS_BASE_URL
        self.api_key_query = BACKEND_POLITICS_API_KEY_QUERY


class BillList(BaseForPoliticsAPIGW, Resource):
    def get(self):
        resource = '/bill/'
        text = self.get_object_from_request(resource)
        return text


class BillDetail(BaseForPoliticsAPIGW, Resource):
    def get(self, id):
        resource = '/bill/%s' % id
        text = self.get_object_from_request(resource)
        return text


def add_resources(api):
    service_prefix = '/politics/'
    api.add_resource(BillList, service_prefix)
    api.add_resource(BillDetail, service_prefix + '<string:id>/')

    return api
