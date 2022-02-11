from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='templates/frontend/static')


@app.route("/")
def index():
    return render_template("frontend/index.html")
