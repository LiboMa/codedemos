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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>ArgoCD Dashboard</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-3">ArgoCD Dashboard</h1>
        <p class="text-danger">Python-flask project <strong>v3Beta</strong>.</p>
        <p>With Git actions</p>
        <p>You are hitting: <strong>{}</strong> Running on AWS EKS</p>
        <p><strong>Datetime:</strong> {}</p>
        <div class="mb-3">
            <p>NODE_NAME: {}<br>
            POD_NAME: {}<br>
            POD_IP: {}<br>
            POD_NAMESPACE: {}</p>
        </div>
        <p>Automated pipeline trigger by <a href="https://github.com/LiboMa/codedemos.git" class="link-primary">https://github.com/LiboMa/codedemos.git</a></p>
    </div>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha384-Ltrj3W8wCJNfTltxH5otPfSELCiHbSDE+QvvYYRj9lLqFQGo8f4wrKweR4FAh1J5" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosvn8x+oKEB1Tc30P9VTf2CQC4jMCg8P5F4kdHfVWHs5T4lQ5Hf" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8sh+0JRqPH/0YFSSVxIfhXKDXePIQ7rXIsoP9z" crossorigin="anonymous"></script>
    -->
</body>
</html>
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
