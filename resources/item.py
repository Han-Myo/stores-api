import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, current_identity, jwt_required
from models.item import ItemModel

class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=int, help="This cannot be left blank", required=True)
    parser.add_argument('store_id', type=int, help="Every item needs a store_id", required=True)
    

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404  
        

    def post(self, name):
        if ItemModel.find_name(name):
            return {"message": "An item with name {} already exists.".format(name)}, 400
        
        data = Items.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.upsert()
        except:
            return {"message": "An error occurred while inserting item!"}, 500
            
        return item.json(), 201 #Created
    
   
    
    def delete(self, name):
        item = ItemModel.find_name(name)
        if item:
            item.delete()
        return {"message": "Item deleted from list"}
    
    def put(self, name):
        data = Items.parser.parse_args()

        item = ItemModel.find_name(name)
        
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.upsert()
        
        return item.json()
    


class ItemsList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
