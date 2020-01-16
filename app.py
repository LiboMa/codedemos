#!/usr/bin/env python 

from flask import Flask
app = Flask(__name__)
import datetime as dt

@app.route('/')
def hello_world():
    message='''
    <h2>Python-flask project. Running on openshift(ocp) </h2>
    <p> //OS: CentOs 7, Openshift 3.11//</p>
    <p>{}</p>
    '''.format(dt.datetime.now())
    return message 
