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


# statring point of app
if __name__ == "__name__":
    app.run()
