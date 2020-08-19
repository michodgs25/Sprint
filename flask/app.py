import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'third_milestone_project'
app.config['MONGO_URI'] = 'mongodb+srv://root:r00tUser@mongo-mini-pro.dhhij.mongodb.net/third_milestone_project?retryWrites=true&w=majority'

mongo = pyMongo(app)

@app.route('/')
@app.route('/get_activity')
def get_tasks():
    return render_template("create.html", activity=mongo.db.activity.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)