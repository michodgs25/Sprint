import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def get_login():
    """Define domain pathway to welcome page.

    Args:
    get login: define opening page of the platform.
    Returns:
    the login.html document.
    """
    return render_template("login.html")


@app.route("/tasks")
def tasks():
    """Add user pathway to explore page.

    Args:
    Tasks variable: define explore page, call tasks collection list.
    Returns:
    previous saved tasks from collection, renders explore page template.
    """
    tasks = list(mongo.db.tasks.find())
    return render_template("explore.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """Create route to search database.

    Args:
    Define search& query variables, GET& POST.
    Returns:
    render explore page template& abilty to search tasks.
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("explore.html", tasks=tasks)


@app.route("/home")
def get_home():
    return render_template("home.html")


@app.route("/activity/add", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        """Add new task to database.

        Args:
        request key value pairs from tasks collection.
        POST method to send task to the database.
        Call mongo function mongo.db.tasks.insert_one,
        Call mongo.db.tasks.find().sort("task_name", 1).
        Returns:
        Insert new task to the database.
        Insert new task into the database collection.
        Sort new task in database.
        Redirect user to explore swprints page.
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

        Args:
        if not statement
        Returns:
        error page
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

        Args:
        database collection task object id.
        Create task variable and attach mongo function,
        to find one task in the collection.
        Return:
        updated task in the collection.
        Updated sprint log and redirect to explore page.
        """
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, submit)
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("edit_activity.html", task=task)


@app.route("/activity/delete/<task_id>")
def delete_activity(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
