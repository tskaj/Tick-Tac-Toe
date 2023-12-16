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
    return render_template("index.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    # UpdateD the session data or game state based on the row and column selected
    
    session["board"][row][col] = session["turn"]
    # Added logic to handle the game moves

    # Redirect back to the game page after the move
    return redirect(url_for("game.html"))

@app.route("/reset")
def reset():
    # ResetS the game state or session data
    session.clear()
    return redirect(url_for("game.html"))

#END OF THE GAME
app.run(debug=True)
