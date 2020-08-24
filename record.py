import os
if os.path.exists("env.py"):
  import env

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = os.environ.get("third-milestone-project") 
COLLECTION_NAME = "activities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
        except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    gender = input("Enter Gender > ")
    age = input("Enter age > ")
    activity = input("Choose activity > ")
    describe = input("Describe activity > ")
    difficulty = input("Activity difficulty > ")

    new_doc = {"first": first.lower(), "last": last.lower(), "gender": gender.lower(),
               "age": age.lower(), "activity": activity.lower(), "describe": describe_activity.lower(), "difficulty": activity_difficulty.lower(), }


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()