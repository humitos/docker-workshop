#!/bin/bash

cd /code
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=8080
