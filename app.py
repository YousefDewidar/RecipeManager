import json
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


# region Recipe
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

        ingredients_data = request.form["ingredients"]
        ingredients = json.loads(ingredients_data)

        # logging.debug(f"Selected ingredients: {ingredients_data}")

        # Insert recipe first
        recipe_id = insert_recipe(
            cursor, name, description, cooking_time, user_id, category_id
        )

        # Insert recipe-ingredient relationships
        for ingredient in ingredients:
            insert_recipe_ingredient(
                cursor,
                recipe_id,
                ingredient["id"],
                ingredient["quantity"],
                ingredient["unit"],
            )

        return redirect(url_for("home"))


@app.route("/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    recipe = get_recipe(cursor, recipe_id)

    if not recipe:
        abort(404)

    users = get_all_users(cursor)
    categories = get_all_categories(cursor)

    selected_ingredients = get_recipe_ingredients(cursor, recipe_id)
    ingredients = get_all_ingredients(cursor)

    return render_template(
        "recipe/edit.html",
        recipe=recipe,
        users=users,
        categories=categories,
        selected_ingredients=selected_ingredients,
        ingredients=ingredients,
    )


@app.route("/submit_updaterecipe", methods=["POST"])
def update():
    if request.method == "POST":
        # Update recipe info
        recipe_id = request.form["recipe_id"]
        name = request.form["name"]
        description = request.form["description"]
        cooking_time = request.form["cooking_time"]
        user_id = request.form["user_id"]
        category_id = request.form["category_id"]

        update_recipe(
            cursor, name, description, cooking_time, user_id, category_id, recipe_id
        )

        # Update ingredients
        new_ingredients_data = request.form["ingredients"]
        new_ingredients = json.loads(new_ingredients_data)

        old_ingredients = get_recipe_ingredients(cursor, recipe_id)

        # Convert old ingredients to a set of names for easy comparison
        old_ingredient_names = {ingredient[1] for ingredient in old_ingredients}

        # Insert new ingredients not in old ingredients
        for ingredient in new_ingredients:
            if ingredient["name"] not in old_ingredient_names:
                insert_recipe_ingredient(
                    cursor,
                    recipe_id,
                    ingredient["id"],
                    ingredient["quantity"],
                    ingredient["unit"],
                )

        # Remove old ingredients not in new ingredients
        new_ingredient_names = {ingredient["name"] for ingredient in new_ingredients}
        for ingredient in old_ingredients:
            ingredient_name = ingredient[1]
            ingredient_id = ingredient[0]

            if ingredient_name not in new_ingredient_names:
                delete_recipe_ingredient(cursor, recipe_id, ingredient_id)

        conn.commit()
        return redirect(url_for("home"))


@app.route("/delete/<int:recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):
    recipe = get_recipe(cursor, recipe_id)

    if not recipe:
        abort(404)

    query2 = "DELETE FROM Recipes WHERE recipe_id = ?;"
    cursor.execute(query2, (recipe_id,))
    conn.commit()

    if cursor.rowcount > 0:
        return redirect(url_for("home"))
    else:
        return "Error: Recipe not found or could not be deleted", 404


# Recipe details route
@app.route("/recipe_details/<int:recipe_id>")
def recipe_details(recipe_id):
    recipe = get_recipe(cursor, recipe_id)
    ingredients = get_recipe_ingredients(cursor, recipe_id)

    if not recipe:
        abort(404)

    # Fetch reviews for the recipe
    reviews = get_reviews_for_recipe(cursor, recipe_id)

    return render_template(
        "home/recipe_details.html", recipe=recipe, ingredients=ingredients, reviews=reviews
    )


@app.route("/submit_search", methods=["GET"])
def search():
    if request.method == "GET":
        keyword = request.args.get("keyword")
        results = search_recipe(cursor, keyword)
        return render_template("home/search_result.html", search_results=results)


# endregion


# region User
@app.route("/all_user")
def all_users_with_recipes():
    users = get_all_users(cursor)
    authors_with_recipes = get_authors_with_recipes(cursor)
    logging.debug(f"Recipes with authors: {authors_with_recipes}")
    return render_template(
        "alluser/all_user.html", users=users, authors_with_recipes=authors_with_recipes
    )


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
        return redirect(url_for("all_users_with_recipes"))


@app.route("/user/delete/<int:user_id>")
def delete_user(user_id):

    delete_user_by_id(cursor, user_id)
    return redirect(url_for("all_users_with_recipes"))


@app.route("/user/edit/<int:user_id>")
def edit_user(user_id):

    new_name = request.args.get("name")
    new_age = request.args.get("age")
    new_email = request.args.get("email")

    update_user_by_id(cursor, user_id, new_name, new_age, new_email)
    return redirect(url_for("all_users_with_recipes"))


# endregion


# region Ingredients
@app.route("/ingredients")
def show_ingredients():
    ingredients = get_all_ingredients(cursor)
    return render_template("/ingredient/all_ingredients.html", ingredients=ingredients)


@app.route("/ingredient/create/")
def create_ingredient():
    name = request.args.get("name")

    name_exists = get_ingredient_id(cursor, name)
    if name_exists is not None:
        return "Ingredient Already Exists", 400

    # create new ingredient
    insert_ingredient(cursor, name)

    return redirect(url_for("show_ingredients"))


@app.route("/ingredient/delete/<int:ingredient_id>")
def delete_ingredient(ingredient_id):

    delete_ingredient_by_id(cursor, ingredient_id)
    return redirect(url_for("show_ingredients"))


@app.route("/ingredient/edit/<int:ingredient_id>")
def edit_ingredient(ingredient_id):
    # Get query parameter 'name'
    new_name = request.args.get("name")

    if not new_name:
        return "Name parameter is required", 400

    # Update ingredient name
    update_ingredient_name(cursor, ingredient_id, new_name)

    return redirect(url_for("show_ingredients"))


# Route to add a new review
@app.route("/review/<int:recipe_id>", methods=["POST"])
def add_review(recipe_id):
    if request.method == "POST":
        # تعيين قيمة ثابتة لـ user_id (مثال: user_id = 1)
        user_id = 1  # قيمة ثابتة للمستخدم الذي يضيف المراجعة

        review_text = request.form["review_text"]
        star_rating = request.form["star_rating"]
        
        # إدخال المراجعة في قاعدة البيانات
        insert_review(cursor, user_id, recipe_id, review_text, star_rating)
        return redirect(url_for("recipe_details", recipe_id=recipe_id))



# Route to fetch reviews for a recipe
@app.route("/recipe/<int:recipe_id>")
def view_reviews(recipe_id):
    reviews = get_reviews_for_recipe(cursor, recipe_id)
    return render_template("recipe/edit.html", reviews=reviews, recipe_id=recipe_id)




# Function to get reviews for a recipe
def get_reviews_for_recipe(cursor, recipe_id):
    query = "SELECT u.full_name as user_name, r.review_text, r.star_rating FROM Reviews r JOIN Users u ON r.user_id = u.user_id WHERE r.recipe_id = ?"
    cursor.execute(query, (recipe_id,))
    return cursor.fetchall()

# Function to insert a new review
def insert_review(cursor, user_id, recipe_id, review_text, star_rating):
    query = "INSERT INTO Reviews (user_id, recipe_id, review_text, star_rating) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (user_id, recipe_id, review_text, star_rating))
    cursor.connection.commit()
    
# endregion


@app.route("/submit_newcategory", methods=["POST"])
def submit_newcategory():
    # get category name from request
    data = request.get_json()
    category_name = data.get("category_name", "").strip()

    if category_name:
        category_exists = get_category_by_name(cursor, category_name)

        # See if category already exists before inserting
        if category_exists:
            insert_category(cursor, category_name)


app.run(debug=True)
cursor.close()
conn.close()
