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
    <H1>==ArgoCD Dashboard==</H1>
    <p><h2>Python-flask project v2. </h2></p>
    <p>you are hitting: {} Rnning on AWS EKS</p>
    <p>{}</p>
    <p></p></body>
    '''.format(os.uname().nodename, dt.datetime.now())
    return message


@app.route('/api/mock')
def test_api():
    data = {"message": "Hi there, this app is running on eks/k8s cluster."}
    return json.dumps(data)


@app.route('/api/postdata', methods=('GET','POST'))
def test_api_postdata():
    if request.method == 'GET':
        data = {"message": "Hi there, flask app, postdata api echo message."}
        return json.dumps(data)
    if request.method == 'POST':
        print(pprint.pprint(dir(request)))
        data = request.get_json()
        print(data)
        #response = {'timestamp':time.time(), 'message':data.decode('utf-8')}
        response = {'timestamp':time.ctime(), 'message': data}
        return  jsonify(response)
    return 
    


if __name__ == '__main__':
    app.run(debug=True)
