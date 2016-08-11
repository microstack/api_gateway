from flask import Flask

app = Flask(__name__)


import os

# ex :) MOVIES_BACKEND_BASE_URL = 'http://localhost:8080'
BACKEND_MOVIES_BASE_URL = os.environ.get('BACKEND_MOVIES_BASE_URL')
BACKEND_POLITICS_BASE_URL = os.environ.get('BACKEND_POLITICS_BASE_URL')

API_GW_PORT =  os.environ.get('API_GW_PORT') or 5000
BACKEND_MOVIES_PORT = os.environ.get('BACKEND_MOVIES_PORT') or 80
BACKEND_POLITICS_PORT = os.environ.get('BACKEND_POLITICS_PORT') or 80

BACKEND_POLITICS_API_KEY_QUERY = os.environ.get(
    'BACKEND_POLITICS_API_KEY_QUERY')
