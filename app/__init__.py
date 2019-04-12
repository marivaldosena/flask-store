import os
from flask import Flask, request, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from app.routes import StoreItemResource, StoreResource, StoreListResource

api.add_resource(StoreListResource, '/store', '/stores')
api.add_resource(StoreResource, '/store', '/store/<string:name>')
api.add_resource(StoreItemResource, '/store/<string:name>/item')


@app.route('/')
def home():
    return render_template('index.html')
