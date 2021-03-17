import flask
from flask import Flask, render_template, redirect, Blueprint, url_for, request
import pickle
from io import StringIO
import json as JSON


app = flask.Flask(__name__)


# Load homepage when root of url is loaded
@app.route("/")
def viz_page():
    return render_template('page.html')


# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)
