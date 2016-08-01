import requests
import os

from wsgi import app


@app.route('/movies/')
def movies():
    url = os.environ.get('MOVIES_BACKEND_URL')
    port = os.environ.get('MOVIES_BACKEND_PORT') or '80'
    response = requests.get(url + ':' + port + '/movies/')
    text = response.text
    
    return text
