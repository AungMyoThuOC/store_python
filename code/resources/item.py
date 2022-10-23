import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import Flask, jsonify, request
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'price',
            type = float,
            required = True,
            help = "This field cannot be blank"
        )
    
    parser.add_argument(
        'name',
        type = str,
        request = True,
        help = 'This field cannot be blank'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {"message" : "Item not found"}, 404

    def post(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return {"message" : "Item with this name {} already exist.".format(name)}, 400
        
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {"message" : "An error occured while inserting data."}, 500

        return item.json(), 201
    
    #@jwt_required()
    def delete(self):
        data = request.get_json()
        item = ItemModel.find_item_by_name(data['name'])
        if item:
            ItemModel.delete_from_db()
        return {"message" : "Item delete successfully!"}, 201
       # connection = sqlite3.connect('mydatabase.db')
        #cursor = connection.cursor()

        #query = "DELETE FROM items WHERE name=?"
        #cursor.execute(query, (name))

       # connection.commit()
        #connection.close()
        #return {'message' : 'item deleted'}

    def put (self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_item_by_name(name)
        update_item = ItemModel(name, data['price'])

        if item is None:
            try:
                update_item.insert()
            except:
                return {"message" : "An error occured while inserting data."}, 500
        else:
            try:
                update_item.update()
            except:
                return {"message" : "An error occured while inserting data."}, 500

        return update_item.json()

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('mydatabase')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({"name" : row[0], "price" : row[1]})

        connection.close()
        return {"items" : items}


    #def get(self):

       # data = request.get_json()

        #item_name = data['itemname']

        #connection = sqlite3.connect('mydatabase.db')
        #cursor = connection.cursor()

        #query = "SELECT * FROM item where name = ?"
        #result = cursor.execute(query, (data['itemname'],))
        #row = result.fetchone()

        #connection.close()

        #if row:
         #   return{
          #      "message" : "success",
           #     "date" : {
            #        "name" : row[0],
             #       "price" : row[1],
              #  }
            #}
        #return {'message' : f'{item_name} not found'}, 401

       # req = request.get_json()
       # req_store = req['store_name']
       # req_item = req['item_name']
       # for store in stores:
       #     if req_store == store['name']:
       #         for item in store['items']:
       #             if req_item == item['name']:
       #                 return {'item': item}, 200
       #     return {'message' : f'{req_item} not found'}, 401
       # return {'message' : f'{req_store} not found'}, 401
