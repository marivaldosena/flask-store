from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

stores = [
    {
        'name': 'store1',
        'items':
        [
            {
                'name': 'item1',
                'price': 15.99
            }
        ]
    }
]

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, type=str,
                    help='Name é obrigatório.')


class StoreListResource(Resource):
    def get(self):
        return jsonify({'stores': stores})


class StoreResource(Resource):
    def get(self, name):
        store = [store for store in stores if store['name'] == name]
        if store:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found'})

    def post(self):
        args = parser.parse_args()

        new_store = {
            'name': args.get('name', None),
            'items': []
        }
        stores.append(new_store)

        return jsonify(new_store)


class StoreItemResource(Resource):
    def get(self, name):
        items = [store['items'] for store in stores if store['name'] == name]

        if items:
            return jsonify({'itens': items})
        else:
            return jsonify({'message': 'Store not found'})

    def post(self, name):
        json = request.get_json()

        new_item = {
            'name': json.get('name', None),
            'price': json.get('price', None)
        }

        for store in stores:
            if store['name'] == name:
                store['items'].append(new_item)
                return jsonify(store)

        return jsonify({'message': 'Store not found'})


api.add_resource(StoreListResource, '/store', '/stores')
api.add_resource(StoreResource, '/store', '/store/<string:name>')
api.add_resource(StoreItemResource, '/store/<string:name>/item')


@app.route('/')
def home():
    return render_template('index.html')
