from flask import Flask, redirect, url_for, render_template, request

# initialize flask app
app = Flask(__name__)


# routes

# home route
@app.route('/')
def home():
    """
    home route
    """
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    """
    docstring
    """
    if request.method == "POST":
        # accessing userName from form
        userName_Form = request.form["userName"]
        return redirect(url_for("user", userName = userName_Form))
    else:
        return render_template("login.html")


@app.route("/<userName>")
def user(userName):
    """
    docstring
    """
    return f"<h1>{userName}</h1>"


# statring point of app
if __name__ == "__name__":
    app.run()
