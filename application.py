#importing flaskpython -m flask run
from flask import Flask, render_template,session
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

#creating twmporary directory to store the session data 
app.config["SESSION_FILE_DIR"]=mkdtemp()
app.config["SESSION_PERMANENT"] =False
app.config["SESSION_TYPE"] ="filesystem"
Session(app)

app.route("/")
def index():
    if "board" not in session:
        session["board"]=[[None,None,None],[None,None,None],[None,None,None]]
        session["turn"]="X"

        return render_template("game.html", game= session["board"], turn= session["turn"])
