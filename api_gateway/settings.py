from flask import Flask

app = Flask(__name__)


import os

# ex :) MOVIES_BACKEND_BASE_URL = 'http://localhost:8080'
MOVIES_BASE_URL = os.environ.get('MOVIES_BASE_URL')
