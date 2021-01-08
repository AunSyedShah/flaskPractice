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
    return f"</title>{userName}</title>"


# redirect example
@app.route("/admin")
def admin():
    """
    admin auth page
    """
    # url_for takes the name of view function to redirect
    return redirect(url_for("home"))


# statring point of app
if __name__ == "__name__":
    app.run()
