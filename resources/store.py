from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404


    def post(self, name):
        if StoreModel.find_name(name):
            return {"message": "A store with name {} already exists.".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.upsert()
        except:
            return {"message": "An error occurred while creating a store"}, 500
        
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_name(name)
        if store:
            store.delete()
        
        return {"message": "Store deleted successfully"}



class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}