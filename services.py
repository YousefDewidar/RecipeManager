def get_all_recipes(cursor):
    query = """SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time 
               FROM [dbo].[Recipes] R
               JOIN [dbo].[Users] U ON R.user_id = U.user_id;"""

    cursor.execute(query)
    results = cursor.fetchall()
    return results
  
  
def get_recipe_ingredients(cursor, recipe_id):
    query = """SELECT RI.recipe_id, I.name as ingredient_name, RI.quantity, RI.unit
               FROM [dbo].[Recipe_Ingredients] RI
               JOIN [dbo].[Ingredients] I ON RI.ingredient_id = I.ingredient_id
               WHERE RI.recipe_id = ?;"""

    cursor.execute(query, recipe_id)
    results = cursor.fetchall()
    return results if results else []


def get_all_users(cursor):
    query = """SELECT user_id, full_name FROM Users;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_recipe(cursor, recipe_id):
    query = f"""SELECT recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time, R.user_id, R.category_id, C.name as category_name
                FROM [dbo].[Recipes] R
                join [dbo].[Users] U on R.user_id = U.user_id
                join [dbo].[Category] C on R.category_id = C.category_id
                WHERE R.recipe_id = ?;"""

    cursor.execute(query, recipe_id)
    result = cursor.fetchone()
    return result if result else None


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


def get_all_users(cursor):
    cursor.execute("SELECT user_id, full_name ,age ,email FROM Users;")
    return cursor.fetchall()


def get_user(cursor, user_id):
    query = """SELECT user_id, full_name FROM Users WHERE user_id = ?;"""
    cursor.execute(query, user_id)
    result = cursor.fetchone()

    return result if result else None


def get_all_categories(cursor):
    cursor.execute("SELECT category_id, name FROM Category")
    return cursor.fetchall()


def get_all_ingredients(cursor):
    cursor.execute("SELECT ingredient_id, name FROM Ingredients")
    return cursor.fetchall()


def get_category(cursor, category_id):
    query = """SELECT category_id, name FROM Category WHERE category_id = ?;"""
    cursor.execute(query, category_id)
    result = cursor.fetchone()

    return result if result else None

def get_recipes_with_authors(cursor):
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

def insert_recipe(cursor, name, description, cooking_time, user_id, category_id):
    query = """INSERT INTO Recipes (name, description, cooking_time, user_id, category_id)
              OUTPUT INSERTED.recipe_id
              VALUES (?, ?, ?, ?, ?);"""
    cursor.execute(query, (name, description, cooking_time, user_id, category_id))
    recipe_id = cursor.fetchone()[0]
    cursor.commit()

    return recipe_id


def insert_recipe_ingredient(
    cursor, recipe_id, ingredient_id, quantity=1.0, unit="grams"
):
    query = """INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit)
               VALUES (?, ?, ?, ?);"""
    cursor.execute(query, (recipe_id, ingredient_id, quantity, unit))
    cursor.commit()


def update_recipe(
    cursor, name, description, cooking_time, user_id, category_id, recipe_id
):
    query = """UPDATE Recipes
            SET name = ?, description = ?, cooking_time = ?, user_id = ?, category_id = ?
            WHERE recipe_id = ?"""
    cursor.execute(
        query, (name, description, cooking_time, user_id, category_id, recipe_id)
    )
    cursor.commit()
