from app import db
from flask_login import UserMixin
from flask_SQLAlchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
