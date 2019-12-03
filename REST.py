from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class ReverseString(Resource):
    def post(self):
        parser.add_argument('string', type=str)
        args = parser.parse_args()
        return args['string'][::-1]

api.add_resource(ReverseString, '/reverse')

if __name__ == '__main__':
     app.run(port='5002')
