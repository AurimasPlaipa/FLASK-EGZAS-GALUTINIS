from enum import Enum
from app import db


class Group_ID(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    

class Amount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0)
    

class Description(db.Model):
    __tablename__ = 'description'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    

    def __init__(self,User_ID,Amount,Desciption):
        self.user_ID = User_ID
        self.amount = Amount
        self.description = Description
