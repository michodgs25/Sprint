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
"""Using the python OS method,
which comes under Python’s standard utility modules

OS.environ module provides a portable way of using
operating system dependent functionality.

The OS environ.get in Python is a mapping object
that represents the environmental variables,
in this case the DBNAME, URI and KEY
and returns a dictionary
using the environmental variable
as key and values called from database as value.

Create and configurate a variable named MONGO_DBNAME,
use OS.environ.get function to fetch database name,
from MONGOb and attach to the variable just created.

Use the same method as above calling the mongo URI,
which establishes the connection between mongo and the application.

In addition create secret key variable and fetch that key
from the above database, attaching the value to the
environment variable.

Create pymongo variable and attatch it to the flask app.
"""


@app.route("/")
@app.route("/index")
def get_index():
    return render_template("index.html")
    """Create App.route which is a Python decorator,
    The decorator tells app, that when user visits domain,
    at the given .route(), execute the index() function,
    and renders index.html document.
"""


# create app route
@app.route("/tasks")
# define get tasks
def get_tasks():
    # create tasks variable and call database tasks collection
    tasks = list(mongo.db.tasks.find())
    # render explore sprints template
    return render_template("explore.html", tasks=tasks)
    """Apply same python decorator method as above,
    create tasks variable, use tasks = list(mongo.db.tasks.find()),
    to fetch database collection named tasks&
    attatch to the tasks variable.

    Returns html document, which uses a for loop, 
    to organise tasks.
    """


# create route for searching database with
# the search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    # render explore page template and search results
    return render_template("explore.html", tasks=tasks)
    """Use app.route python decorator method,
    to search through tasks collection using text indexing.
    """


# create app route
@app.route("/home")
def get_home():
# render home template
    return render_template("home.html")


# create app route, call methods with arguments
# which saves data to database and
# to the explore sprint page
# tells python if data is requested to post data
@app.route("/activity/add", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        # call task variable and provide key value pairs
        # the key value pair are taken from database collection named tasks
        task = {
               "task_name": request.form.get("task_name"),
               "task_surname": request.form.get("task_surname"),
               "task_gender": request.form.get("task_gender"),
               "task_age": request.form.get("task_age"),
               "task_activity": request.form.get("task_activity"),
               "task_title": request.form.get("task_title"),
               "task_description": request.form.get("task_description"),
               "task_difficulty": request.form.get("task_difficulty"),
               "task_date": request.form.get("task_date")
        }
        # tell python to insert one task into database when saved
        mongo.db.tasks.insert_one(task)
        flash("Activity Successfully added")
        # redirect user to new page when task is saved
        return redirect(url_for("get_tasks"))
        # find and sort tasks and render redirected page
    task = mongo.db.tasks.find().sort("task_name", 1)
    return render_template("add_activity.html", task=task)


# create app route, call task id from database
# call get and post method, when user modifies data
# python will update the post in both database and explore page
@app.route("/activity/edit/<task_id>", methods=["POST", "GET"])
def edit_activity(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        return render_template("error.html")
    if request.method == "POST":
        # create submit varible
        # attatch same key value pairs from add_activity
        submit = {
            "task_name": request.form.get("task_name"),
            "task_surname": request.form.get("task_surname"),
            "task_gender": request.form.get("task_gender"),
            "task_age": request.form.get("task_age"),
            "task_activity": request.form.get("task_activity"),
            "task_title": request.form.get("task_title"),
            "task_description": request.form.get("task_description"),
            "task_difficulty": request.form.get("task_difficulty"),
            "task_date": request.form.get("task_date")
        }
        # call database collection task id, to update task
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Activity Successfully Updated")
    # find one and sort updated task in database
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("edit_activity.html", task=task)


# create app route, call task id from database collection
@app.route("/activity/delete/<task_id>")
def delete_activity(task_id):
    # call collection id and inform database to remove
    # object id from the collection
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Removed")
    return redirect(url_for("get_tasks"))


# tell python to host page on this server
# call ip address, set in firstly MongoDB and
# secondly in heroku settings
# call backend port to run via selected browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
