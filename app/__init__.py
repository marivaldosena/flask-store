from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        'name': 'Store 1',
        'items':
        [
            {
                'name': 'Item 1',
                'price': 15.99
            }
        ]
    }
]


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
    pass


@app.route('/store')
@app.route('/stores')
def get_all_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass
