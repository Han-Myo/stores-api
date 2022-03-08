from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name): #gets_one_store
        store = StoreModel.find_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404


    def post(self, name): #creates_a_store
        if StoreModel.find_name(name):
            return {"message": "A store with name {} already exists.".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.upsert()
        except:
            return {"message": "An error occurred while creating a store"}, 500
        
        return store.json(), 201

    def delete(self, name): #deletes_a_store
        store = StoreModel.find_name(name)
        if store:
            store.delete()
        
        return {"message": "Store deleted successfully"}



class StoreList(Resource):
    def get(self): #gets_a_list_of_store
        return {"stores": [store.json() for store in StoreModel.query.all()]}