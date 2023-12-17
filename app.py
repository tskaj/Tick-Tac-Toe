from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

# Creating temporary directory to store the session data
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["turn"] = "O"
    return render_template("index.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["board"][row][col] is None:
        session["board"][row][col] = session["turn"]
        session["turn"] = "O" if session["turn"] == "X" else "X"
    return redirect(url_for("index"))

app.run(debug=True)