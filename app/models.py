from app import db


class ProductModel(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f'{self.name} ({self.cost})'

    def __repr__(self):
        return f'{self.name} ({self.cost})'

    def json(self):
        return {'id': self.id, 'name': self.name, 'cost': self.cost}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def __find_by_id(cls, product_id):
        return cls.query.filter(cls.id == product_id)

    @classmethod
    def update_by_id(cls, product_id, **data):
        cls.__find_by_id(product_id).update(data)
        db.session.commit()

    @classmethod
    def delete_by_id(cls, product_id):
        cls.__find_by_id(product_id).delete()
        db.session.commit()
