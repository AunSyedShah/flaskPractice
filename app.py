from flask import Flask, redirect, url_for, render_template

# initialize flask app
app = Flask(__name__)


# routes

# home route
@app.route('/')
def home():
    """
    home route
    """
    return render_template("base.html")


# statring point of app
if __name__ == "__name__":
    app.run()
