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

    envs = os.environ

    node_name = envs.get("NODE_NAME")
    pod_name = envs.get("POD_NAME")
    pod_ip = envs.get("POD_IP")
    pod_namespace = envs.get("POD_NAMESPACE")
    message = '''
    <html>
    <head>
    <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
    <div class="grid text-center">
    <div class="card"><h1>ArgoCD Dashboard</h1>
    <hr>
    <div class="card"></div>
    <p class="header"><h2>Python-flask project <strong>v3Beta</strong>.</h2></p>
    <p>You are hitting: <strong>{}</strong> Running on AWS EKS</p></div>
    <div class="card"><p><b>Datetime:</b> {}</p>
    <p class="info">
        NODE_NAME: {} <br>
        POD_NAME: {} <br>
        POD_IP: {} <br>
        POD_NAMESPACE: {} <br>
    </p></div>
    <div><p>Automated pipeline trigger by <a href="https://github.com/LiboMa/codedemos.git">https://github.com/LiboMa/codedemos.git</a></p></div></div>
</body></html>
    '''.format(os.uname().nodename, dt.datetime.now(),node_name, pod_name, pod_ip, pod_namespace)
    return message


@app.route('/api/mock')
def test_api():
    data = {"message": "Hi there, this app is running on eks/k8s cluster. change from test"}
    return jsonify(data)


@app.route('/api/postdata', methods=('GET','POST'))
def api_postdata():
    if request.method == 'GET':
        data = {"message": "Hi there, flask app, postdata api echo message."}
        return json.dumps(data)
    if request.method == 'POST':
        print(pprint.pprint(dir(request)))
        data = request.get_json()
        #response = {'timestamp':time.time(), 'message':data.decode('utf-8')}
        response = {'timestamp':time.ctime(), 'message': data}
        return  jsonify(response)
    return 
    


if __name__ == '__main__':
    app.run(debug=True)
