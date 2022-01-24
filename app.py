from flask import Flask
from flask_restful import Api
from flask_jwt import JWT



from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Items, ItemsList
from resources.store import Store, StoreList
from db import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "hanmyo"
api = Api(app)
db.init_app(app)


jwt = JWT(app, authenticate, identity) #Creates a new endpoint called /auth



#item_arg = reqparse.RequestParser()
#item_arg.add_argument("name", type=str, help="You must input item name", required=True)
#item_arg.add_argument("price", type=str, help="You must input item price", required=True)




api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == "__main__":
    app.run(port=5500, debug=True)