import os

from views import app


if __name__ == '__main__':
    port = os.environ.get('API_GW_PORT')
    app.run(port=port)
