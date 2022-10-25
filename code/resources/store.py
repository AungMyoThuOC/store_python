from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            return store.json()
        return {"message" : "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_item_by_name(name):
            return {"message" : "A store with the naem '{}' already exist.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message" : "Error while saving item into db"}, 500
        
        return store.json(), 200

    def delete(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()

        return {"message" : "Store Deleted Successfully"}

class StoreList(Resource):
    def get(stlf):
        stores = StoreModel.query.all()
        return {"stores" : [store.json() for store in stores ]} 