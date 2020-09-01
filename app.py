import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("explore.html", tasks=tasks)


@app.route("/get_create_compare")
def get_create_compare():
    return render_template("home-create-compare.html")


@app.route("/get_about")
def get_about():
    return render_template("about.html")


@app.route("/get_create", methods=["GET", "POST"])
def get_create():
    return render_template("create.html")


@app.route("/add_activity")
def add_activity():
    return render_template("add_activity.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
