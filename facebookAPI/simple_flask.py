from os import access
import flask
from flask import request, jsonify
import json, pprint

import requests
import config
from fb_api import facebookAPI


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    t = {'insert' : 'from local'}
    return jsonify(t)

@app.route('/api/v1/createAPI', methods=['GET'])
def createAPI():
    global fb
    if 'app_id' in request.args and 'app_secret' in request.args:
        app_id = request.args['app_id']
        app_secret = request.args['app_secret']
    else:
        return "app_id and app_secret is require."

    fb = facebookAPI(app_id = app_id, app_secret = app_secret)
    return 'Created'


@app.route('/api/v1/get_user_token', methods=['GET'])
def get_user_token():
    global fb
    if 'scope' in request.args and 'redirect' in request.args:
        scope = request.args['scope']
        redirect = request.args['redirect']
    else:
        return "scope and redirect is require."

    return fb.get_user_token(scope=scope, redirect=redirect)

@app.route('/api/v1/set_user_token', methods=['GET'])
def set_user_token():
    global fb
    if 'user_token' in request.args:
        user_token = request.args['user_token']
    else:
        return "user_token is require."

    fb.set_user_token(user_token)
    return 'OKE'

@app.route('/api/v1/set_page_token', methods=['GET'])
def set_page_token():
    global fb
    if 'pageID' in request.args:
        pageID = request.args['pageID']
    else:
        return "pageID is require."

    fb.set_page_token(token = fb.get_page_token(pageID=pageID))
    return 'OKE'

@app.route('/api/v1/get_page_info', methods=['GET'])
def get_page_info():
    global fb
    return fb.get_page_info()

@app.route('/api/v1/get_posts', methods=['GET'])
def get_posts():
    global fb
    if 'objectID' in request.args:
        objectID = request.args['objectID']
    else:
        return "objectID is require."

    return fb.get_posts(objectID)

app.run(host="0.0.0.0", port=80)
