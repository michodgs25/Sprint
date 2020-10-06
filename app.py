import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

# Use OS function to create environment variables.
app = Flask(__name__)
# Create and configurate a variable named MONGO_DBNAME
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
"""Create mongo URI variable.

Call URI from database, establishing the connection
between mongo database& theflask app.

"""
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
"""Connect flask app to Mongo database.

use OS.environ.get function to fetch database name,
from MONGOb and attach to the MONGO_URI variable.

"""
app.secret_key = os.environ.get("SECRET_KEY")
# Create pymongo variable and attatch it to the flask app.
mongo = PyMongo(app)


# Create App.route which is a Python decorator.
# The decorator tells app, when user visits domain,
# at the given .route(), execute the index() function.
@app.route("/")
@app.route("/index")
def get_index():
    # Renders index.html document.
    return render_template("index.html")


# create app route decorator
@app.route("/tasks")
# define get tasks variable
def get_tasks():
    """Fetch database collection.

    Use list(mongo.db.tasks.find()) method,
    to fetch database collection named tasks&
    attatch to the tasks variable.
    render explore sprints template
    Create domain pathway to explore page
"""
    return render_template("explore.html", tasks=tasks)


# create route to search database
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Add methods GET and POST,
    GET requests specific tasks data,
    POST sends data to create update tasks data.
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    # render explore page template and search results
    return render_template("explore.html", tasks=tasks)
    # Use app.route method,to search tasks collection.


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

    """Edit task data.

    Create app route, call task id from database.
    Call get and post method, when user modifies data.
    Python will update the post in both database and explore page.
    Create submit varible

    """


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


@app.route("/activity/delete/<task_id>")
def delete_activity(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Removed")
    return redirect(url_for("get_tasks"))
    """Remove task the database.

    Call collection id using  mongo.db.tasks.remove.
    Inform database to remove task id.
    Flash message, inform user that task has been removed
    return user to explore page domain.
    """


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
"""Tell python to host page on this server.

Call IP address set in MongoDB and heroku settings,
tell the app using the OS.environ method to run the address.
Use the OS.environ.get method to run backend port via the browser.
"""
