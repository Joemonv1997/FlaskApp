from app import *


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

from models import result,User
@app.route("/market/<hello>")
def market(hello):
    return render_template("market.html",im=hello)
@app.route("/register",methods=["GET","POST"])
def rf():
    reg=Register()
    if request.method=="POST":
        us1=User(user_name=reg.user.data,email=reg.email.data,password=reg.passw.data)
        db.session.add(us1)
        db.session.commit()
        return redirect(url_for("cart"))
    return render_template("register.html",form=reg)
@login_required
@app.route("/cart")
def cart():
    i=result()
    return render_template("cart.html",i=i)


@app.route("/login", methods=["GET", "POST"])
def lf():
    li = Login()
    if request.method=="POST":
        u = User.query.filter_by(
            email=li.email.data).first()
        if u and u.check_password(li.passw.data):
            print("Login Successfull")
        login_user(u)
            return redirect(url_for('cart'))
        else:
            print("Incorrect Password and email")
    return render_template("login.html", form=li)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('lf'))