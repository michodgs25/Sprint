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


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    task = {
        "task_name": request.form.get("task_name"),
        "task_surname": request.form.get("task_surname"),
        "task_gender": request.form.getlist("task_gender"),
        "task_age": request.form.get("task_age"),
        "task_activity": request.form.get("task_activity"),
        "task_title": request.form.get("task_title"),
        "task_description": request.form.get("task_description"),
        "task_difficulty": request.form.getlist("task_difficulty"),
        "task_date": request.form.get("task_date"),
    }
    if request.method == "POST":
        mongo.db.tasks.insert_one(task)
        flash("Activity Successfully added")
        return redirect(url_for("get_create_compare"))

    return render_template("add_activity.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
