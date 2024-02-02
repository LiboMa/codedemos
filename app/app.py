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
    <html><body>
    <H1 color="#3cb371">==ArgoCD Dashboard ==</H1>
    <p><h2>Python-flask project v2. </h2></p>
    <p><h2>With Git actions </h2></p>
    <p>you are hitting: <h2>{}</h2> Rnning on AWS EKS</p>
    <p><b>Datetime: </b>{}</p>
    <p>
        NODE_NAME: {} <br/>
        POD_NAME: {} <br/>
        POD_IP: {} <br/>
        POD_NAMESPACE: {} <br/>
    </p>
    <p>===Automated pipeline trigger by https://github.com/LiboMa/codedemos.git === </p>
    <p> </p></body></html>
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
