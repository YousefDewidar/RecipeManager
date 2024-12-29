# Retrieves all recipes with their author names, descriptions, and cooking times.


def get_all_recipes(cursor):
    query = """
  SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time 
  FROM Recipes R
  JOIN authors U ON R.user_id = U.user_id;
  """

    cursor.execute(query)
    results = cursor.fetchall()
    return results


# Retrieves the ingredients for a specific recipe, including quantity and unit.


def get_recipe_ingredients(cursor, recipe_id):
    query = """
  SELECT I.ingredient_id, I.name as ingredient_name, RI.quantity, RI.unit
  FROM Recipe_Ingredients RI
  JOIN Ingredients I ON RI.ingredient_id = I.ingredient_id
  WHERE RI.recipe_id = %s;
  """

    cursor.execute(query, (recipe_id,))  # Use parameter substitution for security
    results = cursor.fetchall()
    return results if results else []


# Retrieves detailed information about a specific recipe, including category and author.


def get_recipe(cursor, recipe_id):
    query = """
  SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time, C.name as category_name
  FROM Recipes R
  JOIN authors U ON R.user_id = U.user_id
  JOIN Category C ON R.category_id = C.category_id
  WHERE R.recipe_id = %s;
  """

    cursor.execute(query, (recipe_id,))  # Use parameter substitution for security
    result = cursor.fetchone()
    return result if result else None


# Searches for recipes by keyword in their name or description.


def search_recipe(cursor, keyword):
    if not keyword or keyword.strip() == "":
        pass
    else:
        query = """
    SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time
    FROM Recipes R
    JOIN authors U ON R.user_id = U.user_id
    WHERE R.name ILIKE %s OR R.description ILIKE %s;
    """

        search_pattern = f"%{keyword}%"
        cursor.execute(
            query, (search_pattern, search_pattern)
        )  # Use parameter substitution for security
        results = cursor.fetchall()
        return results if results else None


# Inserts a new recipe into the database and returns the inserted recipe's ID.


def insert_recipe(cursor, name, description, cooking_time, user_id, category_id):
    query = """
    INSERT INTO Recipes (name, description, cooking_time, user_id, category_id)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING recipe_id;
    """

    cursor.execute(query, (name, description, cooking_time, user_id, category_id))
    recipe_id = cursor.fetchone()[0]
    return recipe_id


def insert_recipe_ingredient(
    cursor, recipe_id, ingredient_id, quantity=1.0, unit="grams"
):
    query = """
    INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit)
    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(query, (recipe_id, ingredient_id, quantity, unit))


def delete_recipe_ingredient(cursor, recipe_id, ingredient_id):
    query = """DELETE FROM Recipe_Ingredients
               WHERE recipe_id = %s AND ingredient_id = %s;"""
    cursor.execute(query, (recipe_id, ingredient_id))


def update_recipe(
    cursor, name, description, cooking_time, user_id, category_id, recipe_id
):
    query = """UPDATE Recipes
            SET name = %s, description = %s, cooking_time = %s, user_id = %s, category_id = %s
            WHERE recipe_id = %s"""
    cursor.execute(
        query, (name, description, cooking_time, user_id, category_id, recipe_id)
    )


# Retrieves all users with their IDs, names, ages, and emails.
def get_all_users(cursor):
    cursor.execute("SELECT user_id, full_name, age, email FROM authors;")
    return cursor.fetchall()


# Retrieves all authors (users) with their corresponding recipes.
def get_authors_with_recipes(cursor):
    query = """SELECT 
                    u.full_name AS user_name,
                    r.name AS recipe_name,
                    r.recipe_id
                FROM 
                    Recipes r
                JOIN 
                    authors u
                ON 
                    r.user_id = u.user_id;"""

    cursor.execute(query)
    results = cursor.fetchall()
    return results


# Retrieves a specific user's ID and name based on their user_id.


def get_user(cursor, user_id):
    query = """SELECT user_id, full_name FROM authors WHERE user_id = %s;"""
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    return result if result else None


# Deletes a user by their user_id.
def delete_user_by_id(cursor, user_id):
    query = """DELETE FROM authors
                WHERE user_id = %s;"""
    cursor.execute(query, (user_id,))


# Updates a user's information (name, age, email) by their user_id.
def update_user_by_id(cursor, user_id, new_name, new_age, new_email):
    query = """UPDATE authors
                SET full_name = %s, age = %s, email = %s
                WHERE user_id = %s;"""
    cursor.execute(query, (new_name, new_age, new_email, user_id))


# Retrieves all categories with their IDs and names.
def get_all_categories(cursor):
    cursor.execute("SELECT category_id, name FROM Category")
    return cursor.fetchall()


# Retrieves a specific category by its category_id.
def get_category(cursor, category_id):
    query = """SELECT category_id, name FROM Category WHERE category_id = %s;"""
    cursor.execute(query, (category_id,))
    result = cursor.fetchone()

    return result if result else None


def get_category_by_name(cursor, category_name):
    query = """SELECT category_id FROM Category WHERE name = %s;"""
    cursor.execute(query, (category_name,))
    result = cursor.fetchone()

    return result if result else None


def insert_category(cursor, category_name):
    query = "INSERT INTO Category (name) VALUES (%s);"
    cursor.execute(query, (category_name,))


# Inserts a new ingredient into the Ingredients table.
def insert_ingredient(cursor, ingredient_name):
    query = """INSERT INTO Ingredients (name)
                VALUES (%s)"""

    cursor.execute(query, (ingredient_name,))
    return


# Retrieves the ingredient ID for a given ingredient name.
def get_ingredient_id(cursor, ingredient_name):
    query = """SELECT ingredient_id FROM Ingredients
                WHERE name = %s"""

    cursor.execute(query, (ingredient_name,))
    result = cursor.fetchone()
    return result if result else None


# Updates the name of an ingredient by its ingredient_id.
def update_ingredient_name(cursor, ingredient_id, new_name):
    query = """UPDATE Ingredients
                SET name = %s
                WHERE ingredient_id = %s;"""

    cursor.execute(query, (new_name, ingredient_id))
    return


# Deletes an ingredient by its ingredient_id.
def delete_ingredient_by_id(cursor, ingredient_id):
    query = """DELETE FROM Ingredients
                WHERE ingredient_id = %s;"""

    cursor.execute(query, (ingredient_id,))
    return


# Retrieves all ingredients with their IDs and names.
def get_all_ingredients(cursor):
    cursor.execute("SELECT ingredient_id, name FROM Ingredients")
    return cursor.fetchall()


# Function to get reviews for a recipe
def get_reviews_for_recipe(cursor, recipe_id):
    query = """
        SELECT r.review_id, r.reviewer_name as user_name, r.review_text, r.star_rating, r.is_edited
        FROM Reviews r 
        WHERE r.recipe_id = %s
    """
    cursor.execute(query, (recipe_id,))
    return cursor.fetchall()


# Function to insert a new review
def insert_review(cursor, recipe_id, review_text, reviewer_name, star_rating):
    query = "INSERT INTO Reviews (recipe_id, review_text, reviewer_name, star_rating) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (recipe_id, review_text, reviewer_name, star_rating))


def delete_review_by_id(cursor, review_id):
    query = """DELETE FROM Reviews WHERE review_id = %s;"""
    cursor.execute(query, (review_id,))
    return


def update_review_by_id(cursor, review_id, reviewer_name, review_text, star_rating):
    query = """UPDATE Reviews
            SET reviewer_name = %s, review_text = %s, star_rating = %s
            WHERE review_id = %s"""
    cursor.execute(query, (reviewer_name, review_text, star_rating, review_id))
