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


# Recipe details route
@app.route("/recipe_details/<int:recipe_id>")
def recipe_details(recipe_id):
    recipe = get_recipe(cursor, recipe_id)
    ingredients = get_recipe_ingredients(cursor, recipe_id)

    if not recipe:
        abort(404)

    return render_template("home/recipe_details.html", recipe=recipe, ingredients=ingredients)


# Recipe routes
@app.route("/create")
def create_recipe():
    users = get_all_users(cursor)
    categories = get_all_categories(cursor)
    ingredients = get_all_ingredients(cursor)
    return render_template(
        "recipe/create.html",
        users=users,
        categories=categories,
        ingredients=ingredients,
    )


@app.route("/submit_newrecipe", methods=["POST"])
def submit_newrecipe():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        cooking_time = request.form["cooking_time"]
        user_id = request.form["user_id"]
        category_id = request.form["category_id"]

        ingredient_ids = request.form.getlist("ingredient_id[]")
        logging.debug(f"Selected ingredients: {ingredient_ids}")

        # Insert recipe first
        recipe_id = insert_recipe(
            cursor, name, description, cooking_time, user_id, category_id
        )

        # Insert recipe-ingredient relationships
        for ingredient_id in ingredient_ids:
            insert_recipe_ingredient(cursor, recipe_id, ingredient_id)

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


# new delete
@app.route("/delete/<int:recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):
    recipe = get_recipe(cursor, recipe_id)

    if not recipe:
        abort(404)

    query1 = "DELETE FROM Recipe_Ingredients WHERE recipe_id = ?;"
    cursor.execute(query1, (recipe_id,))

    query2 = "DELETE FROM Recipes WHERE recipe_id = ?;"
    cursor.execute(query2, (recipe_id,))
    conn.commit()

    if cursor.rowcount > 0:
        return redirect(url_for("home"))
    else:
        return "Error: Recipe not found or could not be deleted", 404

#   check (old delet)
# @app.route("/delete/<int:recipe_id>")
# def delete_recipe(recipe_id):
#     recipe = get_recipe(cursor, recipe_id)

#     if not recipe:
#         abort(404)

#     return render_template("recipe/delete.html", recipe=recipe)


# @app.route("/submit_deleterecipe", methods=["POST"])
# def delete():
#     recipe_id = request.form["recipe_id"]

#     query1 = f"DELETE FROM Recipe_Ingredients WHERE recipe_id = ?;"
#     cursor.execute(query1, recipe_id)

#     query2 = f"DELETE FROM Recipes WHERE recipe_id = ?;"
#     cursor.execute(query2, recipe_id)
#     conn.commit()

#     if cursor.rowcount > 0:
#         # Deletion was successful
#         return redirect(url_for("home"))
#     else:
#         # Deletion failed (recipe_id not found)
#         return "Error: Recipe not found or could not be deleted", 404

# -----------------------------------

@app.route("/submit_search", methods=["GET"])
def search():
    if request.method == "GET":
        keyword = request.args.get("keyword")
        results = search_recipe(cursor, keyword)
        return render_template("home/search_result.html", search_results=results)


# User routes
@app.route("/all_user")
def all_users_with_recipes():
    users = get_all_users(cursor)
    recipes_with_authors = get_recipes_with_authors(cursor)
    logging.debug(f"Recipes with authors: {recipes_with_authors}")
    return render_template("alluser/all_user.html", users=users, recipes_with_authors=recipes_with_authors)

# all_user old replaced by all_users_with_recipes
# The /all_user_with_recipes route displays both users and their associated recipes, 
# while the /all_user route only shows a list of users without any recipe information.


@app.route("/create_authour")
def create_author():
    return render_template("autour/create_authour.html")


@app.route("/submit_newauthor", methods=["POST"])
def submit_newauthor():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form.get("age")
        email = request.form.get("email")
        query = """INSERT INTO Users(full_name,age,email)
                  VALUES (?,?,?);"""

        cursor.execute(query, (name, age, email))
        conn.commit()
        return redirect(url_for("home"))


app.run(debug=True)
cursor.close()
conn.close()
