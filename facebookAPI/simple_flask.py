from os import access
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    if 'access_token' in request.args:
        access_token = request.args['access_token']
    print(access_token)
    return access_token

app.run(host="0.0.0.0", ssl_context='adhoc')