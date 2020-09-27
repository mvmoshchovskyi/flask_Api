from flask_restful import Resource, request
from .models import ProductModel


class ProductResource(Resource):
    def get(self):
        products = ProductModel.query.all()
        return [item.json() for item in products], 200

    def post(self):
        data = ProductModel(**request.form)
        data.save_to_db()
        return data.json(), 201

    def patch(self, product_id):
        ProductModel.update_by_id(product_id, **request.form)
        return {'message': ' product was updated'}, 200

    def delete(self, product_id):
        ProductModel.delete_by_id(product_id)
        return {'message': ' product was deleted'}, 200
