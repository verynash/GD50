import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helper import apology, apology2, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///ZJC.db")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # logout

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    # register new user
    if request.method == "POST":
        #check for errors and inserts user into users table
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        if not username:
            return apology2("username required")
        elif not email:
            return apology2("email required")
        elif not password:
            return apology2("password required")
        elif not confirm:
            return apology2("confirm password")
        if password != confirm:
            return apology2("passwords do not match")
        userconfirm = db.execute("SELECT username FROM users WHERE username = ?", username)
        if not userconfirm:
            passhash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, email, hash) VALUES (?, ?, ?)", username, email, passhash)
            return redirect("/")
        else:
            return apology2("username taken")

        #log in: zach, zach1
    else:
        #display registration form
        return render_template("register.html")


@app.route("/")

def homepage():
    return render_template("homepage.html")

@app.route("/kicks")
def kicks():
    return render_template("kicks.html")

@app.route("/apparel")
def apparel():
    return render_template("apparel.html")

@app.route("/rts")
def rts():
    return render_template("rts.html")

@app.route("/order")
@login_required
def order():
    inventory = db.execute("SELECT item, size, logo, printed, handpainted FROM inventory")
    return render_template("order.html", inventory=inventory)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")
