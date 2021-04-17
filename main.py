from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)


class FoodModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.String(100), nullable=True)
    date_expires = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Food(id={self.id}, name={self.name}, date_added={self.date_added}, date_expires={self.date_expires})"


food_put_args = reqparse.RequestParser()
food_put_args.add_argument(
    "name", type=str, help="name of the food is required", required=True)
food_put_args.add_argument("date_added", type=str,
                           help="date of the added food")
food_put_args.add_argument("date_expires", type=str,
                           help="estimated expire date of the food")


food_patch_args = reqparse.RequestParser()
food_patch_args.add_argument("date_added", type=str,
                             help="date of the added food")
food_patch_args.add_argument("date_expires", type=str,
                             help="estimated expire date of the food")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'date_added': fields.String,
    'date_expires': fields.String
}


class Food(Resource):
    @marshal_with(resource_fields)
    def get(self, food_id):
        result = FoodModel.query.filter_by(id=food_id).first()
        if not result:
            abort(404, message=f"food_id: {food_id} doesnt exist")
        return result, 200

    @marshal_with(resource_fields)
    def put(self, food_id):
        result = FoodModel.query.filter_by(id=food_id).first()
        if result:
            abort(409, message=f"food_id {food_id} already exists")
        args = food_put_args.parse_args()
        food = FoodModel(
            id=food_id, name=args['name'], date_added=args['date_added'], date_expires=args['date_expires'])
        db.session.add(food)
        db.session.commit()
        return food, 201

    @marshal_with(resource_fields)
    def patch(self, food_id):
        result = FoodModel.query.filter_by(id=food_id).first()
        if not result:
            abort(404, message=f"food_id: {food_id} doesnt exist")
        args = food_patch_args.parse_args()
        if args['date_added']:
            result.name = args['date_added']
        if args['date_expires']:
            result.name = args['date_expires']
        return result, 200

    @marshal_with(resource_fields)
    def delete(self, food_id):
        result = FoodModel.query.filter_by(id=food_id).first()
        if not result:
            abort(404, message=f"food_id: {food_id} doesnt exist")
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(Food, "/food/<int:food_id>")

if __name__ == '__main__':
    app.run(debug=True)
