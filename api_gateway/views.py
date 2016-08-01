import requests
import os

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/movies/')
def movies():
    url = os.environ.get('MOVIES_BACKEND_URL')
    port = os.environ.get('MOVIES_BACKEND_PORT') or '80'
    response = requests.get(url + ':' + port + '/movies/')
    text = response.text

    return text

if __name__ == '__main__':
    port = os.environ.get('API_GW_PORT')
    app.run(port=port)
