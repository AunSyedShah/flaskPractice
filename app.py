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
    numbers_list = [2, 3, 4, 5, 6]
    context = {
        "numbers": numbers_list
    }
    return render_template("base.html", context=context)


# statring point of app
if __name__ == "__name__":
    app.run()
