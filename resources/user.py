

from flask_restful import Resource, reqparse
from models.user import UserModel



    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, help="Cannot be left blank", required=True)
    parser.add_argument("password", type=str, help="Cannot be left blank", required=True)


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exist"}

        user = UserModel(data['username'], data['password'])
        
        try:
            user.upsert()
        except:
            return {"message": "Sorry error in the server"}, 500
    
        return {"message": "User created successfully"}, 201
