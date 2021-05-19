from app import *
from app import db

class User(UserMixin,db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    user_name=db.Column(db.String(length=100),nullable=True)
    email=db.Column(db.String(length=100),nullable=True)
    password=db.Column(db.String(length=100),nullable=True)
    def check_password(self,p):
        if self.password==p:
            return True

def result():
    rer=User.query.all()
    return rer
