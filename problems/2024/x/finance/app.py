import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    symbol = db.execute(
        "SELECT * FROM purchases WHERE user_id = ?", session["user_id"]
    )
    return symbol


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol_input = request.form.get("symbol")

        try:
            shares_input = int(request.form.get("shares"))
        except ValueError:
            return apology("must provide shares", 403)

        if symbol_input == None:
            return apology("must provide symbol", 403)
        elif lookup(symbol_input) == None:
            return apology("invalid symbol", 400)
        elif shares_input < 1:
            return apology("invalid shares", 400)

        stock_price = lookup(symbol_input)["price"]
        total = shares_input * stock_price
        current_datetime = datetime.now()
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )

        db.execute(
            "INSERT INTO purchases (user_id, symbol, shares, price, total, purchase_date) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], symbol_input, shares_input, stock_price, total, current_datetime
        )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol_input = request.form.get("symbol")
        quote = lookup(symbol_input)

        if symbol_input == None:
            return apology("must provide symbol", 403)

        elif quote == None:
            return apology("invalid symbol", 400)

        else:
            return render_template("quoted.html", symbol_input=symbol_input, quote=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        password_hash = generate_password_hash(password_input)
        confirmation_input = request.form.get("confirmation")

        if not username_input:
            return apology("must provide username", 403)

        elif not password_input:
            return apology("must provide password", 403)

        elif not password_input == confirmation_input:
            return apology("passwords do not match", 403)

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username_input, password_hash
            )
            register_status = "Successfully registered your account!"
        except ValueError:
            return apology("username already exists", 403)

        return render_template("/", register_status=register_status)

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
