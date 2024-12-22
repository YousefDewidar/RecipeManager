from os import getenv

import pyodbc
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from services import *

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Connection to the SQL Server
server = getenv("DB_SERVER", ".")  # Fallback to '.' if not set
database = getenv("DB_NAME", "recipe")  # Fallback to 'recipe' if not set

conn = pyodbc.connect(
    f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


# Main App View
@app.route("/")
def home():
    result = get_all_recipes(cursor)
    return render_template("home/home.html", recipes=result)


@app.route("/create")
def create_recipe():
    users = get_all_users(cursor)
    categories = get_all_categories(cursor)
    return render_template("recipe/create.html", users=users, categories=categories)


@app.route("/submit_newrecipe", methods=["POST"])
def submit_newrecipe():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        cooking_time = request.form["cooking_time"]
        user_id = request.form["user_id"]
        category_id = request.form["category_id"]

        query = """INSERT INTO Recipes (name, description, cooking_time, user_id, category_id)
                  VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (name, description, cooking_time, user_id, category_id))
        conn.commit()

        return redirect(url_for("home"))


@app.route("/submit_search", methods=["GET"])
def search():
    if request.method == "GET":
        keyword = request.args.get("searchName")
        results = search_recipe(cursor, keyword)
        return render_template("results.html", search_results=results)


@app.route("/submit_updaterecipe", methods=["POST"])
def update():
    if request.method == "POST":
        recipe_id = request.form["recipeID"]
        recipe_name = request.form["recipeName"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        update_recipe(cursor, conn, recipe_id, recipe_name, quantity, price)
        return render_template("index.html")


@app.route("/submit_deleterecipe", methods=["POST"])
def delete():
    if request.method == "POST":
        recipe_id = request.form["recipeID"]
        successful = delete_recipe(cursor, conn, recipe_id)
        if successful:
            return render_template("index.html")
        else:
            return render_template("fail.html")


app.run(debug=True)
cursor.close()
conn.close()
