from flask import Flask, redirect, url_for

# initialize flask app
app = Flask(__name__)


# routes

# home route
@app.route('/')
def home():
    """
    home route
    """
    return "Aun Syed Shah"


@app.route('/<userName>')
def user(userName):
    """
    userName page
    """
    return f"<h1>Welcome {userName}</h1>"


# redirect example
@app.route("/admin")
def admin():
    """
    admin auth page
    """
    # url_for takes the name of view function to redirect
    # we can also provide arguments to url_for fucntion while redirect
    return redirect(url_for("user", userName="Aun Syed Shah"))


# statring point of app
if __name__ == "__name__":
    app.run()
