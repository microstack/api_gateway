from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


from .movies import MovieList, add_resources

api = add_resources(api)
