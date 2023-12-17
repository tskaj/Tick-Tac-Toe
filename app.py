from flask import Flask, render_template, session, redirect, url_for, request
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
    result = request.args.get("result", default=None, type=str)
    return render_template("index.html", game=session["board"], turn=session["turn"], result=result)

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["board"][row][col] is None:
        session["board"][row][col] = session["turn"]
        session["turn"] = "O" if session["turn"] == "X" else "X"
    result = check_winner()
    return redirect(url_for("index", result=result))

@app.route("/restart")
def restart():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"
    session["turn"] = "O"
    return redirect(url_for("index"))


def check_winner():
    for i in range(3):
        x_win = True
        o_win = True
        for j in range(3):
            if session["board"][i][j] == "X":
                o_win = False
            elif session["board"][i][j] == "O":
                x_win = False
            else:
                x_win = False
                o_win = False
        if x_win:
            return "Player X wins"
        if o_win:
            return "Player O wins"
        
    for i in range(3):
        x_win = True
        o_win = True
        for j in range(3):
            if session["board"][j][i] == "X":
                o_win = False
            elif session["board"][j][i] == "O":
                x_win = False
            else:
                x_win = False
                o_win = False
        if x_win:
            return "Player X wins"
        if o_win:
            return "Player O wins"
        
    x_win = True
    o_win = True
    for i in range(3):
        if session["board"][i][i] == "X":
            o_win = False
        elif session["board"][i][i] == "O":
            x_win = False
        else:
            x_win = False
            o_win = False
    if x_win:
        return "Player X wins"
    if o_win:
        return "Player O wins"
    
    x_win = True
    o_win = True
    for i in range(3):
        if session["board"][i][2-i] == "X":
            o_win = False
        elif session["board"][i][2-i] == "O":
            x_win = False
        else:
            x_win = False
            o_win = False
    if x_win:
        return "Player X wins"
    if o_win:
        return "Player O wins"
    
    game_over = True

    for i in range(3):
        for j in range(3):
            if session["board"][i][j] == None:
                game_over = False

    if game_over:
        return "The Match has tied"
    
    return ""


app.run(debug=True)