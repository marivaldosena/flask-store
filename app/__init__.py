from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    json = request.get_json()
    new_store = {
        'name': json.get('name', None),
        'items': []
    }
    stores.append(new_store)

    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    store = [store for store in stores if store['name'] == name]
    if store:
        return jsonify(store)
    else:
        return jsonify({'message': 'Store not found'})


@app.route('/store')
@app.route('/stores')
def get_all_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
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


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    items = [store['items'] for store in stores if store['name'] == name]

    if items:
        return jsonify({'itens': items})
    else:
        return jsonify({'message': 'Store not found'})
