# -*- coding: utf-8 -*-

import os

from flask.ext.pymongo import PyMongo
from flask import Flask, request, redirect, render_template
from bson.objectid import ObjectId

MONGO_URL = os.environ.get(
    'MONGO_URL',
    'mongodb://eject:eject@ds041583.mongolab.com:41583/series')
app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)


@app.route("/")
def index():
    series = mongo.db.series.find()
    return render_template("index.html", series=series)


@app.route("/series/add/")
def serie_add_form():
    return render_template("add.html")


@app.route("/series/add/", methods=['POST'])
def serie_add():
    mongo.db.series.insert(request.form.to_dict())
    return redirect('/')


@app.route("/series/<serie_id>/edit/")
def series_edit_form(serie_id):
    serie = mongo.db.series.find_one(ObjectId(serie_id))
    return render_template("edit.html", serie=serie)


@app.route("/series/<serie_id>/edit/", methods=['POST'])
def series_edit(serie_id):
    serie = mongo.db.series.find_one(ObjectId(serie_id))
    serie.update(request.form.to_dict())
    mongo.db.series.save(serie)
    return redirect('/')


@app.route("/series/<serie_id>/delete/")
def process_delete(serie_id):
    mongo.db.series.remove(ObjectId(serie_id))
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
