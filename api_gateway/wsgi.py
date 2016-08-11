import os

from api.settings import app
from settings import API_GW_PORT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_GW_PORT)
