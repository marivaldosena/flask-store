from flask import request
from flask_restful import Resource
from app.models import db, StoreItem, Store


class StoreItemResource(Resource):
    def get(self, name):
        items = Store.query.filter_by(name=name).first().items

        if items:
            return {'itens': [item.to_json() for item in items]}
        else:
            return {'message': 'Store not found'}, 404

    def post(self, name):
        json = request.get_json()

        store = Store.query.filter_by(name=name).first()
        new_item = StoreItem(name=json.get('name', None),
                             price=json.get('price', None))

        store.items.append(new_item)
        return store.to_json()
        db.session.add(store)
        db.session.commit()


        if store:
            return store, 201

        return {'message': 'Store not found'}, 404
