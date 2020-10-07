import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
"""Create app and environment variables.

Use OS function to create environment variables.
Create and configurate a variable named MONGO_DBNAME
"""
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
"""Connect flask app to the MongoDb database.

Create MONGO_URI variable, use OS.get function,
calling the MONGO_URI string and attaching the string,
to the MONGO_URI variable.
"""
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
"""Access the database.

Create secret_key variable and use the OS function,
to attach the SECRET_KEY to secret_key variable.
"""
app.secret_key = os.environ.get("SECRET_KEY")
# Create pymongo variable and attatch it to the flask app.
mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def get_index():
    """
    Create App.route which is a Python decorator.
    The decorator tells app, when user visits domain,
    at the given .route(), execute the index() function.
    Renders index.html document.
    """
    return render_template("index.html")


@app.route("/tasks")
def tasks():
    """Add user pathway to explore page.

    Define tasks variable
    Attach database task collection to tasks variable.
    Return explore page template.
    """
    tasks = list(mongo.db.tasks.find())
    return render_template("explore.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Create route to search database.

    Define search variable.

    Create query variable,
    use request.form.get method to obtain,
    task data variables and attach to the query variable.

    Create tasks variable, use mongo function,
    list(mongo.db.tasks.find to search title& description,
    set in mongodb.

    Return explore page template.
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("explore.html", tasks=tasks)


# create app route
@app.route("/home")
def get_home():
    """Add new tasks to database.

    Create app route saving data to the database.
    Request POST method to send task to the database.
    Create task variable and attach key values that matches
    the tasks collection values.
    Render home template and renders homepage index.html.
    """
    return render_template("home.html")


@app.route("/activity/add", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        """Add new tasks to database.

        Create app route saving data to the database.
        Request POST method to send task to the database.
        Create task variable and attach key values that matches
        the tasks collection values.
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

        Use mongo function mongo.db.tasks.insert_one,
        to insert new task into the database collection.

        Flask message informs user the task has been added.

        App redirects user to explore page when log is saved.

        Call task variable and use mongo function:
        mongo.db.tasks.find().sort to sort task in the collection,
        and redirect to create page template.
        """
        mongo.db.tasks.insert_one(task)
        flash("Activity Successfully added")
        return redirect(url_for("tasks"))
    task = mongo.db.tasks.find().sort("task_name", 1)
    return render_template("add_activity.html", task=task)


@app.route("/activity/edit/<task_id>", methods=["POST", "GET"])
def edit_activity(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        """Return error page if log does not exist.

        Add if not statement, which app returns error page,
        when a log no longer exists.
        """
        return render_template("error.html")
    if request.method == "POST":
        """Allow user to edit tasks.

        create the submit varible,
        and attach the same key value pairs
        from add_activity function.

        Use mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit),
        to update task in the database.
        """
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
        """Update task in the database collection.

        Call database collection task object id,
        to update& submit task,
        and call flash message,
        to inform user that task has been updated.

        Create task variable, attach mongo function,
        to find one task in the collection.

        Sort updated task in the collection,
        using the mongo function mongo.db.tasks.find_one.
        and return edit page template.
        """
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Activity Successfully Updated")
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("edit_activity.html", task=task)


@app.route("/activity/delete/<task_id>")
def delete_activity(task_id):
    """Allow user to delete tasks.

    Use mongo.db.tasks.remove({"_id": ObjectId(task_id)}),
    to remove the task from the database.

    Once task is deleted, flash message informs user of this,
    and page redirects to the explore page with all search results.
    """
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Removed")
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    """Connect flask app to Mongo database.

    use OS.environ.get function to fetch database name,
    from MONGOb and attach to the MONGO_URI variable.
    """
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
