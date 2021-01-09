from flask import Flask, redirect, url_for, render_template, request, session

# initialize flask app
app = Flask(__name__)

#secret key
app.secret_key = "aunsyedshah"

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
        # storing user data to session key
        session["user_session"] = userName_Form
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    """
    docstring
    """
    # check if there is any data in session
    if "user_session" in session:
        user = session["user_session"]
        return f"<h1>{user}</h1>"
    else:
        return f"No User in session yet!"


# statring point of app
if __name__ == "__name__":
    app.run()
