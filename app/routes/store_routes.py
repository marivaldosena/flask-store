from flask_restful import Resource, reqparse
from app.models import Store, db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, type=str,
                    help='Name é obrigatório.')


class StoreListResource(Resource):
    def get(self):
        stores = [store.to_json() for store in Store.query.all()]
        return {'stores': stores}


class StoreResource(Resource):
    def get(self, name):
        store = Store.query.filter_by(name=name).first()

        if store:
            return store.to_json()
        else:
            return {'message': 'Store not found'}, 404

    def post(self):
        args = parser.parse_args()

        new_store = Store(name=args.get('name', None))

        db.session.add(new_store)
        db.session.commit()

        return new_store.to_json(), 201
