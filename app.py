from flask import Flask, render_template, url_for, request, redirect, flash
import pam
from flask_login import UserMixin, LoginManager, login_required, logout_user, login_user




app = Flask(__name__)
app.config['SECRET_KEY'] = "kachong" #Dette skal ligges i en secret fil.


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


"""
login_manager sørger for at vi bruger flask-login 
Det bruger vores app variabel, og at login vieweren bliver bruger vores form fra login.html
"""



#login_manager.session_protection = "strong"
#login_manager.session_protection = "basic"



class User(UserMixin): #Vi nedarver UserMixin objekterne for at kunne bruge is_authenticate osv.
    def __init__(self, username):
        self.id = username




@login_manager.user_loader
def load_user(user_id):
    return User(user_id)





username1 = "surin"
password1 = "1234"

testbruger = User(username1)

@app.route("/") #@ = Decorator
def home():
    return render_template("home.html")



@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        if username == username1 and password == password1:
            login_user(testbruger)
            return redirect(url_for("home"))
        else:
            return render_template("login.html")
    #if pam.authenticate(user, password, servie='login'):



@app.route("/data")
@login_required
def data():
    if testbruger.is_authenticated == True:
        return render_template("data.html")
    else:
        flash("Mangler login.")
        return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(debug=True, port=5000,)