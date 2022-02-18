"""Module contains flask app which buids UI"""

from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='templates/frontend/static')
app.input_config = []


@app.route("/", methods=['GET'])
def index():
    """renders main react app"""
    return render_template("frontend/index.html")


@app.route('/api/config')
def config():
    """returns list of input component configurations"""
    component_config = {"input": app.input_config, "output": []}
    return jsonify(component_config)


@app.route('/api/func', methods=['POST'])
def func():
    """Runs user function on input values"""
    data = request.json
    print(data)
