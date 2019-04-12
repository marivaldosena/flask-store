from app import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    items = db.relationship('StoreItem', backref='store', lazy=False)

    def __str__(self):
        return '<Store: {}>'.format(self.name)

    def __repr__(self):
        return '<Store: {}>'.format(self.name)


class StoreItem(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    price = db.Column(db.Float)
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.id'), nullable=False)

    def __str__(self):
        return '<Item: {}>'.format(self.name)

    def __repr__(self):
        return '<Item: {}>'.format(self.name)
