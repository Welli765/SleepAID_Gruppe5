from flask import Flask, render_template, url_for, request, redirect
import pam
import flask_login
from flask_login import UserMixin




app = Flask(__name__)
app.config['SECRET_KEY'] = "kachong" #Dette skal ligges i en secret fil.
PAM = ""


username1 = "surin"
password1 = "1234"

"""""
class User():
    id1 = ""
    username1 = ""
    password1 = ""


testbruger_UID = "503"

"""


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
            return redirect(url_for("data"))
        else:
            return render_template("login.html")
    #if pam.authenticate(user, password, servie='login'):



@app.route("/data")
def data():
    return render_template("data.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000,)

#login_manager = flask_login.LoginManager()

#login_manager.init_app(app)
