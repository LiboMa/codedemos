#!/usr/bin/env python 

from flask import Flask
app = Flask(__name__)
import json
import datetime as dt

@app.route('/')
def hello_world():
    message='''
    <h2>Python-flask project. Running on openshift(OKD env all-in-one) </h2>
    <p> //OS: CentOs 7, Openshift 3.11//</p>
    <p>{}</p>
    '''.format(dt.datetime.now())
    return message

@app.route('/api/mock')
def test_api():

    data = {"message":"Hi there, this app is running on ODK-openshift 3.11"}
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
