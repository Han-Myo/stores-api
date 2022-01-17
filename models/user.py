
from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()
    
    def upsert(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()
        