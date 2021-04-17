from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)

food_put_args = reqparse.RequestParser()
food_put_args.add_argument("name", type=str, help="name of the food")
food_put_args.add_argument("date_added", type=str,
                           help="date of the added food")
food_put_args.add_argument("date_added", type=str,
                           help="date of the added food")

food = {}


class Food(Resource):
    def get(self, name):
        return food[name]

    def put(self, name):
        args = food_put_args.parse_args()
        return {name: args}


api.add_resource(Food, "/cats/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
