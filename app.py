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


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        task = {
               "task_name": request.form.get("task_name"),
               "task_surname": request.form.get("task_surname"),
               "task_gender": request.form.getlist("task_gender"),
               "task_age": request.form.get("task_age"),
               "task_activity": request.form.getlist("task_activity"),
               "task_title": request.form.get("task_title"),
               "task_description": request.form.getlist("task_description"),
               "task_difficulty": request.form.getlist("task_difficulty"),
               "task_date": request.form.get("task_date")
        }
        mongo.db.tasks.insert_one(task)
        flash("Activity Successfully added")
        return redirect(url_for("get_tasks"))
        
    tasks = mongo.db.tasks.find().sort("task_name", 1)
    return render_template("add_activity.html", tasks=tasks)
                

@app.route("/edit_activity/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    
        submit = {
               "task_name": request.form.get("task_name"),
               "task_surname": request.form.get("task_surname"),
               "task_gender": request.form.getlist("task_gender"),
               "task_age": request.form.get("task_age"),
               "task_activity": request.form.getlist("task_activity"),
               "task_title": request.form.get("task_title"),
               "task_description": request.form.getlist("task_description"),
               "task_difficulty": request.form.getlist("task_difficulty"),
               "task_date": request.form.get("task_date")
        }
        
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Activity Successfully Updated")
        return redirect(url_for('get_tasks'))
        
        task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
        task = mongo.db.tasks.find().sort("task_name", 1)
        return render_template("edit_activity.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)