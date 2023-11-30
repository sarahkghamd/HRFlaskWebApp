from tkinter import CASCADE
from . import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(150), nullable=False)
