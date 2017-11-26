# -*- coding: utf-8 -*-


from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = []
    try:
        response.append(requests.get('http://restrictions:8080/').text)
    except:
        response.append('Error contacting RESTRICTIONS')

    try:
        response.append(requests.get('http://users:8080/').text)
    except:
        response.append('Error contacting USERS')

    try:
        response.append(requests.get('http://locations:8080/').text)
    except:
        response.append('Error contacting LOCATIONS')

    return '<br>'.join(response)
