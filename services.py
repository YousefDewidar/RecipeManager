# Retrieves all recipes with their author names, descriptions, and cooking times.
def get_all_recipes(cursor):
    query = """SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time 
               FROM [dbo].[Recipes] R
               JOIN [dbo].[Users] U ON R.user_id = U.user_id;"""

    cursor.execute(query)
    results = cursor.fetchall()
    return results


# Retrieves the ingredients for a specific recipe, including quantity and unit.
def get_recipe_ingredients(cursor, recipe_id):
    query = """SELECT I.ingredient_id, I.name as ingredient_name, RI.quantity, RI.unit
               FROM [dbo].[Recipe_Ingredients] RI
               JOIN [dbo].[Ingredients] I ON RI.ingredient_id = I.ingredient_id
               WHERE RI.recipe_id = ?;"""

    cursor.execute(query, recipe_id)
    results = cursor.fetchall()
    return results if results else []


# Retrieves detailed information about a specific recipe, including category and author.
def get_recipe(cursor, recipe_id):
    cursor.execute("EXEC spGetRecipeById @recipe_id = ?", recipe_id)
    result = cursor.fetchone()
    return result if result else None


# Searches for recipes by keyword in their name or description.
def search_recipe(cursor, keyword):
    if not keyword or keyword.strip() == "":
        pass
    else:
        query = """SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time
                   FROM [dbo].[Recipes] R
                   JOIN [dbo].[Users] U ON R.user_id = U.user_id
                   WHERE R.name LIKE ? OR R.description LIKE ?;"""

        search_pattern = f"%{keyword}%"
        cursor.execute(query, (search_pattern, search_pattern))
        results = cursor.fetchall()
        return results if results else None


# Retrieves all authors (users) with their corresponding recipes.
def get_authors_with_recipes(cursor):
    query = """SELECT 
                    u.full_name AS user_name,
                    r.name AS recipe_name,
                    r.recipe_id
               FROM 
                    [dbo].[Recipes] r
               JOIN 
                    [dbo].[Users] u
               ON 
                    r.user_id = u.user_id;"""

    cursor.execute(query)
    results = cursor.fetchall()
    return results


# Inserts a new recipe into the database and returns the inserted recipe's ID.
def insert_recipe(cursor, name, description, cooking_time, user_id, category_id):
    query = """INSERT INTO Recipes (name, description, cooking_time, user_id, category_id)
              OUTPUT INSERTED.recipe_id
              VALUES (?, ?, ?, ?, ?);"""
    cursor.execute(query, (name, description, cooking_time, user_id, category_id))
    recipe_id = cursor.fetchone()[0]
    cursor.commit()

    return recipe_id


# Inserts a new ingredient for a specific recipe.
def insert_recipe_ingredient(cursor, recipe_id, ingredient_id, quantity=1.0, unit="grams"):
    query = """INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit)
               VALUES (?, ?, ?, ?);"""
    cursor.execute(query, (recipe_id, ingredient_id, quantity, unit))
    cursor.commit()


def delete_recipe_ingredient(cursor, recipe_id, ingredient_id):
    query = """DELETE FROM Recipe_Ingredients
               WHERE recipe_id = ? AND ingredient_id = ?;"""
    cursor.execute(query, (recipe_id, ingredient_id))
    cursor.commit()


def update_recipe(
    cursor, name, description, cooking_time, user_id, category_id, recipe_id
):
    query = """UPDATE Recipes
            SET name = ?, description = ?, cooking_time = ?, user_id = ?, category_id = ?
            WHERE recipe_id = ?"""
    cursor.execute(query, (name, description, cooking_time, user_id, category_id, recipe_id))
    cursor.commit()


# Retrieves all users with their IDs, names, ages, and emails.
def get_all_users(cursor):
    cursor.execute("SELECT user_id, full_name ,age ,email FROM Users;")
    return cursor.fetchall()


# Retrieves a specific user's ID and name based on their user_id.
def get_user(cursor, user_id):
    query = """SELECT user_id, full_name FROM Users WHERE user_id = ?;"""
    cursor.execute(query, user_id)
    result = cursor.fetchone()

    return result if result else None


# Deletes a user by their user_id.
def delete_user_by_id(cursor, user_id):
    query = """DELETE FROM Users
               WHERE user_id = (?);"""
    cursor.execute(query, user_id)
    cursor.commit()


# Updates a user's information (name, age, email) by their user_id.
def update_user_by_id(cursor, user_id, new_name, new_age, new_email):
    query = """UPDATE Users
               SET full_name = ?, age = ?, email = ?
               WHERE user_id = ?;"""
    cursor.execute(query, (new_name, new_age, new_email, user_id))
    cursor.commit()


# Retrieves all categories with their IDs and names.
def get_all_categories(cursor):
    cursor.execute("SELECT category_id, name FROM Category")
    return cursor.fetchall()


# Retrieves a specific category by its category_id.
def get_category(cursor, category_id):
    query = """SELECT category_id, name FROM Category WHERE category_id = ?;"""
    cursor.execute(query, category_id)
    result = cursor.fetchone()

    return result if result else None


# Inserts a new ingredient into the Ingredients table.
def insert_ingredient(cursor, ingredient_name):
    query = """INSERT INTO Ingredients (name)
               values (?)"""

    cursor.execute(query, ingredient_name)
    cursor.commit()
    return


# Retrieves the ingredient ID for a given ingredient name.
def get_ingredient_id(cursor, ingredient_name):
    query = """SELECT ingredient_id FROM Ingredients
               WHERE name = (?)"""

    cursor.execute(query, ingredient_name)
    result = cursor.fetchone()
    return result if result else None


# Updates the name of an ingredient by its ingredient_id.
def update_ingredient_name(cursor, ingredient_id, new_name):
    query = """UPDATE Ingredients
               SET name = (?)
               WHERE ingredient_id = (?);"""

    cursor.execute(query, new_name, ingredient_id)
    cursor.commit()
    return


# Deletes an ingredient by its name.
def delete_ingredient_by_name(cursor, ingredient_name):
    query = """DELETE FROM Ingredients
               WHERE name = (?);"""

    cursor.execute(query, ingredient_name)
    cursor.commit()
    return


# Deletes an ingredient by its ingredient_id.
def delete_ingredient_by_id(cursor, ingredient_id):
    query = """DELETE FROM Ingredients
               WHERE ingredient_id = (?);"""

    cursor.execute(query, ingredient_id)
    cursor.commit()
    return


# Retrieves all ingredients with their IDs and names.
def get_all_ingredients(cursor):
    cursor.execute("SELECT ingredient_id, name FROM Ingredients")
    return cursor.fetchall()

# Inserts a new review into the Reviews table.
def insert_review(cursor, user_id, recipe_id, review_text):
    query = """INSERT INTO Reviews (user_id, recipe_id, review_text)
               OUTPUT INSERTED.review_id
               VALUES (?, ?, ?);"""
    cursor.execute(query, (user_id, recipe_id, review_text))
    review_id = cursor.fetchone()[0]
    cursor.commit()
    return review_id

# Retrieves all reviews for a specific recipe.
def get_reviews_for_recipe(cursor, recipe_id):
    query = """SELECT R.review_id, U.full_name as author_name, R.review_text
               FROM Reviews R
               JOIN Users U ON R.user_id = U.user_id
               WHERE R.recipe_id = ?;"""
    cursor.execute(query, recipe_id)
    return cursor.fetchall()


