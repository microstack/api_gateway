# -*- encoding: utf-8 -*-
import requests
import os

from flask_restful import Resource

import os, sys
sys.path.append(os.path.abspath('..'))

from api.base import BaseForAPIGW
from api_gateway.settings import POLITICS_BASE_URL


class BaseForPoliticsAPIGW(BaseForAPIGW):
    def __init__(self):
        self.base_url = POLITICS_BASE_URL
        self.api_query = '?api_key=test'


class BillList(BaseForPoliticsAPIGW, Resource):
    def get(self):
        resource = '/bill/'
        text = self.response_text_from_request(resource+self.api_query)
        return text


class BillDetail(BaseForPoliticsAPIGW, Resource):
    def get(self, id):
        resource = '/bill/%d' % id
        text = self.response_text_from_request(resource+self.api_query)
        return text


def add_resources(api):
    api.add_resource(BillList, '/bills/')
    api.add_resource(BillDetail, '/bills/<int:id>/')

    return api
