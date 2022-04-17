from models.user import UserModel
from werkzeug.security import safe_str_cmp
#from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

users = [
    UserModel("hanmyogeorge", "immaculate"),
    UserModel('prettyokanezi', 'rumuodogo'),
    UserModel("onyeanunaeze", "eze1"),
    UserModel("davidjaja", "daiveed"),
    UserModel("kogamkate", "salvation"),
    UserModel("peacegeorge", "amadipeace")]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username) #username_table.get(username, None)(for in-memory database)
    if user and safe_str_cmp(user.password, password): 
        return user
        

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id) #userid_table.get(user_id, None)