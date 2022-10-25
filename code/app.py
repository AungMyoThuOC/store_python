from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
# from item import Item

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# from item import Items

app = Flask(__name__)

app.config['SQLALCHEMY_DQTABASE_URI'] = "sqlit:///mydatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'onii-chan yemete'
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, 'stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)