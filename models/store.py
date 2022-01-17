from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    item = db.relationship("ItemModel", lazy="dynamic")
    
    
    def  __init__(self, name):
        self.name = name
        
    
    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.item.all()]}
    
    @classmethod
    def find_name(cls, name):
        return StoreModel.query.filter_by(name=name).first()
        
    
    def upsert(self):
        db.session.add(self)
        db.session.commit()
        
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    