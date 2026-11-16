from flask import Flask
from simplepam import authenticate
import flask_login



app = Flask(__name__)
app.secret_key = "kachong"

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

@app.route("/")
def home():
    return "Hello World"

home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
