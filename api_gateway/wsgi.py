import os

from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    port = os.environ.get('API_GW_PORT')
    app.run(port=port)
