from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


from . import movies
from . import politics

api = movies.add_resources(api)
api = politics.add_resources(api)
