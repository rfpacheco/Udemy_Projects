# Flask example copied from http://flask.pocoo.org/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Version 2"
