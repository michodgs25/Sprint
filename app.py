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
    Args:
    get index: define opening page of the platform.
    Returns:
    the index.html document.
    """
    return render_template("index.html")


@app.route("/sprints")
def sprints():
    """Add user pathway to explore page.

    Args:
    Tasks variable: define explore page, call sprints collection list.
    Returns:
    previous saved tasks from collection, renders explore page template.
    """
    sprints = list(mongo.db.sprints.find())
    return render_template("explore.html", sprints=sprints)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Create route to search database.

    Args:
    Define search& query variables, GET& POST.
    Returns:
    render explore page template& abilty to search sprints.
    """
    query = request.form.get("query")
    sprints = list(mongo.db.sprints.find({"$text": {"$search": query}}))
    return render_template("explore.html", sprints=sprints)


@app.route("/home")
def get_home():
    return render_template("home.html")


@app.route("/activity/add", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        """Add new sprint to database.

        Args:
        request key value pairs from sprints collection.
        POST method to send sprint to the database.
        Call mongo function mongo.db.sprint.insert_one,
        Call mongo.db.sprints.find().sort("sprint_name", 1).
        Returns:
        Insert new sprint into database.
        Insert new sprint into the database collection.
        Sort new sprint in database.
        Redirect user to explore sprints page.
        """
        sprint = {
               "sprint_name": request.form.get("sprint_name"),
               "sprint_surname": request.form.get("sprint_surname"),
               "sprint_gender": request.form.get("sprint_gender"),
               "sprint_age": request.form.get("sprint_age"),
               "sprint_activity": request.form.get("sprint_activity"),
               "sprint_title": request.form.get("sprint_title"),
               "sprint_description": request.form.get("sprint_description"),
               "sprint_difficulty": request.form.get("sprint_difficulty"),
               "sprint_date": request.form.get("sprint_date")
        }
        mongo.db.sprints.insert_one(sprint)
        return redirect(url_for("sprints"))
    sprint = mongo.db.sprints.find().sort("sprint_name", 1)
    return render_template("add_activity.html", sprint=sprint)


@app.route("/activity/edit/<sprint_id>", methods=["POST", "GET"])
def edit_activity(sprint_id):
    """Create app route to edit page.

    Copy:
    sprint_id variable from mongoDb.
    Add:
    methods GET and POST
    Define:
    edit_activity variable.
    Attach:
    task_id to edit_activity variable
"""
    sprint = mongo.db.sprints.find_one({"_id": ObjectId(sprint_id)})
    if not sprint:
        """Return error page if log does not exist.

        Args:
        if not statement
        Returns:
        error page
        """
        return render_template("error.html")
    if request.method == "POST":
        submit = {
            "sprint_name": request.form.get("sprint_name"),
            "sprint_surname": request.form.get("sprint_surname"),
            "sprint_gender": request.form.get("sprint_gender"),
            "sprint_age": request.form.get("sprint_age"),
            "sprint_activity": request.form.get("sprint_activity"),
            "sprint_title": request.form.get("sprint_title"),
            "sprint_description": request.form.get("sprint_description"),
            "sprint_difficulty": request.form.get("sprint_difficulty"),
            "sprint_date": request.form.get("sprint_date")
        }
        mongo.db.sprints.update({"_id": ObjectId(sprint_id)}, submit)
        return redirect(url_for("sprints"))
        """Update sprint in the database collection.

        Args:
        database collection sprint object id.
        Create sprint variable and attach mongo function,
        to find one sprint in the collection.
        Return:
        updated sprint in the collection.
        Updated sprint log and redirect to explore page.
        """
        mongo.db.sprints.update_one({"_id": ObjectId(sprint_id)}, submit)
    sprint = mongo.db.sprints.find_one({"_id": ObjectId(sprint_id)})
    return render_template("edit_activity.html", sprint=sprint)


@app.route("/activity/delete/<sprint_id>")
def delete_activity(sprint_id):
    mongo.db.sprints.remove({"_id": ObjectId(sprint_id)})
    return redirect(url_for("sprints"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
