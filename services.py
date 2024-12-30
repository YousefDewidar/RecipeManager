from utils import _execute_query

# Retrieves all recipes with their author names, descriptions, and cooking times.


def get_all_recipes():
    query = """
    SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time
    FROM Recipes R
    JOIN authors U ON R.user_id = U.user_id;
    """
    return _execute_query(query)


# Retrieves the ingredients for a specific recipe, including quantity and unit.


def get_recipe_ingredients(recipe_id):
    query = """
    SELECT I.ingredient_id, I.name as ingredient_name, RI.quantity, RI.unit
    FROM Recipe_Ingredients RI
    JOIN Ingredients I ON RI.ingredient_id = I.ingredient_id
    WHERE RI.recipe_id = %s;
    """
    return _execute_query(query, (recipe_id,))


# Retrieves detailed information about a specific recipe, including category and author.


def get_recipe(recipe_id):
    query = """
    SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time, C.name as category_name
    FROM Recipes R
    JOIN authors U ON R.user_id = U.user_id
    JOIN Category C ON R.category_id = C.category_id
    WHERE R.recipe_id = %s;
    """
    rows = _execute_query(query, (recipe_id,))
    return rows[0] if rows else None


# Searches for recipes by keyword in their name or description.


def search_recipe(keyword):
    if not keyword or keyword.strip() == "":
        return []
    query = """
    SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time
    FROM Recipes R
    JOIN authors U ON R.user_id = U.user_id
    WHERE R.name ILIKE %s OR R.description ILIKE %s;
    """
    pattern = f"%{keyword}%"
    return _execute_query(query, (pattern, pattern))


# Inserts a new recipe into the database and returns the inserted recipe's ID.


def insert_recipe(name, description, cooking_time, user_id, category_id):
    query = """
    INSERT INTO Recipes (name, description, cooking_time, user_id, category_id)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING recipe_id;
    """
    result = _execute_query(
        query, (name, description, cooking_time, user_id, category_id)
    )
    return result[0][0] if result else None


def delete_recipe_by_id(recipe_id):
    query = """
    DELETE FROM Recipes
    WHERE recipe_id = %s;
    """
    return _execute_query(query, (recipe_id,))


def insert_recipe_ingredient(recipe_id, ingredient_id, quantity=1.0, unit="grams"):
    query = """
    INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit)
    VALUES (%s, %s, %s, %s);
    """
    _execute_query(query, (recipe_id, ingredient_id, quantity, unit))


def delete_recipe_ingredient(recipe_id, ingredient_id):
    query = """
    DELETE FROM Recipe_Ingredients
    WHERE recipe_id = %s AND ingredient_id = %s;
    """
    _execute_query(query, (recipe_id, ingredient_id))


def update_recipe(name, description, cooking_time, user_id, category_id, recipe_id):
    query = """
    UPDATE Recipes
    SET name = %s, description = %s, cooking_time = %s, user_id = %s, category_id = %s
    WHERE recipe_id = %s
    """
    _execute_query(
        query, (name, description, cooking_time, user_id, category_id, recipe_id)
    )


# Retrieves all users with their IDs, names, ages, and emails.
def get_all_users():
    query = "SELECT user_id, full_name, age, email FROM authors;"
    return _execute_query(query)


# Retrieves all authors (users) with their corresponding recipes.
def get_authors_with_recipes():
    query = """
    SELECT u.full_name AS user_name, r.name AS recipe_name, r.recipe_id
    FROM Recipes r
    JOIN authors u ON r.user_id = u.user_id;
    """
    return _execute_query(query)


# Retrieves a specific user's ID and name based on their user_id.


def get_user(user_id):
    query = "SELECT user_id, full_name FROM authors WHERE user_id = %s;"
    rows = _execute_query(query, (user_id,))
    return rows[0] if rows else None


# Deletes a user by their user_id.
def delete_user_by_id(user_id):
    query = "DELETE FROM authors WHERE user_id = %s;"
    _execute_query(query, (user_id,))


# Updates a user's information (name, age, email) by their user_id.
def update_user_by_id(user_id, new_name, new_age, new_email):
    query = """
    UPDATE authors
    SET full_name = %s, age = %s, email = %s
    WHERE user_id = %s;
    """
    _execute_query(query, (new_name, new_age, new_email, user_id))


# Retrieves all categories with their IDs and names.
def get_all_categories():
    query = "SELECT category_id, name FROM Category"
    return _execute_query(query)


# Retrieves a specific category by its category_id.
def get_category(category_id):
    query = "SELECT category_id, name FROM Category WHERE category_id = %s;"
    rows = _execute_query(query, (category_id,))
    return rows[0] if rows else None


def get_category_by_name(category_name):
    query = "SELECT category_id FROM Category WHERE name = %s;"
    rows = _execute_query(query, (category_name,))
    return rows[0] if rows else None


def insert_category(category_name):
    query = "INSERT INTO Category (name) VALUES (%s);"
    _execute_query(query, (category_name,))


# Inserts a new ingredient into the Ingredients table.
def insert_ingredient(ingredient_name):
    query = "INSERT INTO Ingredients (name) VALUES (%s)"
    _execute_query(query, (ingredient_name,))


# Retrieves the ingredient ID for a given ingredient name.
def get_ingredient_id(ingredient_name):
    query = """
    SELECT ingredient_id FROM Ingredients
    WHERE name = %s
    """
    rows = _execute_query(query, (ingredient_name,))
    return rows[0] if rows else None


# Updates the name of an ingredient by its ingredient_id.
def update_ingredient_name(ingredient_id, new_name):
    query = """
    UPDATE Ingredients
    SET name = %s
    WHERE ingredient_id = %s;
    """
    _execute_query(query, (new_name, ingredient_id))


# Deletes an ingredient by its ingredient_id.
def delete_ingredient_by_id(ingredient_id):
    query = "DELETE FROM Ingredients WHERE ingredient_id = %s;"
    _execute_query(query, (ingredient_id,))


# Retrieves all ingredients with their IDs and names.
def get_all_ingredients():
    query = "SELECT ingredient_id, name FROM Ingredients"
    return _execute_query(query)


# Function to get reviews for a recipe
def get_reviews_for_recipe(recipe_id):
    query = """
    SELECT r.review_id, r.reviewer_name as user_name, r.review_text, r.star_rating, r.is_edited
    FROM Reviews r 
    WHERE r.recipe_id = %s
    """
    return _execute_query(query, (recipe_id,))


# Function to insert a new review
def insert_review(recipe_id, review_text, reviewer_name, star_rating):
    query = """
    INSERT INTO Reviews (recipe_id, review_text, reviewer_name, star_rating)
    VALUES (%s, %s, %s, %s)
    """
    _execute_query(query, (recipe_id, review_text, reviewer_name, star_rating))


def delete_review_by_id(review_id):
    query = "DELETE FROM Reviews WHERE review_id = %s;"
    _execute_query(query, (review_id,))


def update_review_by_id(review_id, reviewer_name, review_text, star_rating):
    query = """
    UPDATE Reviews
    SET reviewer_name = %s, review_text = %s, star_rating = %s
    WHERE review_id = %s
    """
    _execute_query(query, (reviewer_name, review_text, star_rating, review_id))
