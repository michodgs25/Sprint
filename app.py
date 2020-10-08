import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
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
@app.route("/index")
def get_index():
    """Define domain pathway to welcome page.

    Create:
    App.route which is a Python decorator.
    Decorator:
    tells app, when user visits domain,
    at the given .route(), execute the index() function.
    Return:
    the index.html document.
    """
    return render_template("index.html")


@app.route("/tasks")
def tasks():
    """Add user pathway to explore page.

    Define:
    tasks variable.
    Attach:
    database task collection to tasks variable.
    Return:
    explore page template document.
    """
    tasks = list(mongo.db.tasks.find())
    return render_template("explore.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Create route to search database.

    Define:
    search variable.
    Create:
    query variable.
    Apply:
    request.form.get method to obtain,
    task data variables and attach to the query variable.
    Create:
    tasks variable, use mongo function,
    list(mongo.db.tasks.find to search title& description,
    set in mongodb.
    Return:
    explore page template.
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("explore.html", tasks=tasks)


@app.route("/home")
def get_home():
    """Create route to homepage.

    Define:
    get_home variable.
    return:
    homepage html template.
    """
    return render_template("home.html")


@app.route("/activity/add", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        """Add new task to database.

        Create:
        app route saving data to the database tasks collection,
        and intial methods GET AND POST.
        Request:
        POST method to send task to the database.
        Create:
        task variable and attach key values,
        that matches the tasks collection values.
        """
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
        """Save new Sprint logs to the tasks collection.

        Apply:
        mongo function mongo.db.tasks.insert_one,
        to insert new task into the database collection.
        Flash message:
        informs user the task has been added.
        App:
        redirects user to explore page when log is saved.
        Call:
        task variable.
        Use mongo function:
        mongo.db.tasks.find().sort to sort task in the collection,
        Redirect:
        to create page.
        """
        mongo.db.tasks.insert_one(task)
        return redirect(url_for("tasks"))
    task = mongo.db.tasks.find().sort("task_name", 1)
    return render_template("add_activity.html", task=task)


@app.route("/activity/edit/<task_id>", methods=["POST", "GET"])
def edit_activity(task_id):
    """Create app route to edit page.

    Copy:
    task_id variable from mongoDb.
    Add:
    methods GET and POST
    Define:
    edit_activity variable.
    Attach:
    task_id to edit_activity variable
"""
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        """Return error page if log does not exist.

        Add:
        if not statement, which app returns error page,
        when:
        a log no longer exists.
        """
        return render_template("error.html")
    if request.method == "POST":
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
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        return redirect(url_for("tasks"))
        """Update task in the database collection.

        Call:
        database collection task object id.
        Update:
        submit task, and call flash message,
        to inform user that task has been updated.
        Create:
        task variable and attach mongo function,
        to find one task in the collection.
        Sort:
        updated task in the collection.
        Apply:
        mongo function mongo.db.tasks.find_one.
        Return:
        edit page template.
        """
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, submit)
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("edit_activity.html", task=task)


@app.route("/activity/delete/<task_id>")
def delete_activity(task_id):
    """Allow user to delete tasks.

        Apply:
        mongo.db.tasks.remove({"_id": ObjectId(task_id)}),
        to remove the task from the database.
        Task is deleted:
        flash message informs user of this.
        Redirect:
        to the explore page with all logs.
        """
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
