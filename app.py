from models import *
from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,LoginManager,logout_user,login_required
from werkzeug.urls import url_parse
app=Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///market.db"
app.config['SECRET_KEY']='4c045f6962abd95e343c4750'
loginapp = LoginManager(app)
loginapp.login_view="lf"
from forms import *
from routes import *
if __name__=="__main":
    app.run(debug=True)
