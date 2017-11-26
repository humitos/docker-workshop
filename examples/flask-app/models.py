# -*- coding: utf-8 -*-

from app import db


class Timestamp(db.Model):
    __tablename__ = 'timestamp'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime())

    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __repr__(self):
        return '<id: {} | timestamp: {}>'.format(self.id, self.timestamp)
