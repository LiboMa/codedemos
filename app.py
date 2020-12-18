#!/usr/bin/env python 

from flask import Flask, request, redirect, render_template, jsonify
import time

app = Flask(__name__)
import json
import datetime as dt
import os
import pprint


@app.route('/')
def index():
    message = '''
    <body>
    <p><h2>Python-flask project V2. </h2></p>
    <p>{} </p>
    <p>{}</p></body>
    '''.format(os.uname().version, dt.datetime.now())
    return message


@app.route('/api/mock')
def test_api():
    data = {"message": "Hi there, this app is running on k8s cluster"}
    return json.dumps(data)


@app.route('/api/postdata', methods=('GET','POST'))
def test_api_postdata():
    if request.method == 'GET':
        data = {"message": "Hi there, flask app, postdata api echo message."}
        return json.dumps(data)
    if request.method == 'POST':
        data = request.json
        print(pprint.pprint(dir(request)))
        #response = {'timestamp':time.time(), 'message':data.decode('utf-8')}
        response = {'timestamp':time.ctime(), 'message': data}
        return  jsonify(response)
    return 
    


if __name__ == '__main__':
    app.run(debug=True)
