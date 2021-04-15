from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)
food = {"Lu": {"age": 5, "gender": "male"},
        "Lou": {"age": 3, "gender": "female"}}


class Food(Resource):
    def get(self, name):
        return food[name]

    def post(self):
        return {"data": "Posted"}


api.add_resource(Food, "/cats/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
