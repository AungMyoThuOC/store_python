from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
# from item import Item

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

# from item import Items

app = Flask(__name__)

app.secret_key = 'onii-chan yemete'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)