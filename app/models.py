from app import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    items = db.relationship('StoreItem', backref='store', lazy='joined')

    def __str__(self):
        return '{}'.format(self.to_json())

    def __repr__(self):
        return '{}'.format(self.to_json())

    def to_json(self):
        json = {
            'name': self.name,
            'items': [self.items.all]
        }

        return json


class StoreItem(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.id'), nullable=False)

    def __str__(self):
        return '{}'.format(self.to_json())

    def __repr__(self):
        return '{}'.format(self.to_json())

    def to_json(self):
        json = {
            'name': self.name,
            'price': self.price,
            'store_id': self.store_id
        }

        return json
