# -*- coding: utf-8 -*-

import datetime
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import Timestamp
db.create_all()

@app.route('/')
def timestamp():
    t = Timestamp(timestamp=datetime.datetime.now())
    db.session.add(t)
    db.session.commit()
    response = [t.timestamp.isoformat() for t in Timestamp.query.all()]
    return '<br>\n'.join(response)
