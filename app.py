import logging
from os import getenv

import pyodbc
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, url_for

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

logging.basicConfig(level=logging.DEBUG)


# Main App View
@app.route("/")
def home():
    result = get_all_recipes(cursor)
    return render_template("home/home.html", recipes=result)


# Recipe routes
@app.route("/create")
def create_recipe():
    users = get_all_users(cursor)
    categories = get_all_categories(cursor)
    ingredients = get_all_ingredients(cursor)
    return render_template("recipe/create.html", users=users, categories=categories,ingredients=ingredients)


@app.route("/submit_newrecipe", methods=["POST"])
def submit_newrecipe():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        cooking_time = request.form["cooking_time"]
        user_id = request.form["user_id"]
        category_id = request.form["category_id"]

        insert_recipe(cursor, name, description, cooking_time, user_id, category_id)

        return redirect(url_for("home"))


@app.route("/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    recipe = get_recipe(cursor, recipe_id)

    if not recipe:
        abort(404)

    users = get_all_users(cursor)
    categories = get_all_categories(cursor)

    return render_template(
        "recipe/edit.html", recipe=recipe, users=users, categories=categories
    )


@app.route("/submit_updaterecipe", methods=["POST"])
def update():
    if request.method == "POST":
        recipe_id = request.form["recipe_id"]
        name = request.form["name"]
        description = request.form["description"]
        cooking_time = request.form["cooking_time"]
        user_id = request.form["user_id"]
        category_id = request.form["category_id"]
        update_recipe(
            cursor, name, description, cooking_time, user_id, category_id, recipe_id
        )
        return redirect(url_for("home"))


@app.route("/delete/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = get_recipe(cursor, recipe_id)

    if not recipe:
        abort(404)

    return render_template("recipe/delete.html", recipe=recipe)


@app.route("/submit_deleterecipe", methods=["POST"])
def delete():
    recipe_id = request.form["recipe_id"]

    query = f"DELETE FROM Recipes WHERE recipe_id = ?;"
    cursor.execute(query, recipe_id)
    conn.commit()

    if cursor.rowcount > 0:
        # Deletion was successful
        return redirect(url_for("home"))
    else:
        # Deletion failed (recipe_id not found)
        return "Error: Recipe not found or could not be deleted", 404


@app.route("/submit_search", methods=["GET"])
def search():
    if request.method == "GET":
        keyword = request.args.get("keyword")
        results = search_recipe(cursor, keyword)
        return render_template("home/search_result.html", search_results=results)


# User routes
@app.route("/all_user")
def all_users():
    result = get_all_users(cursor)
    return render_template("alluser/all_user.html", users=result)


@app.route("/create_authour")
def create_author():
    return render_template("autour/create_authour.html")


@app.route("/submit_newauthor", methods=["POST"])
def submit_newauthor():
    if request.method == "POST":
        name = request.form["name"]

        query = """INSERT INTO Users(full_name)
                  VALUES (?);"""

        cursor.execute(query, (name))
        conn.commit()
        return redirect(url_for("home"))


app.run(debug=True)
cursor.close()
conn.close()
