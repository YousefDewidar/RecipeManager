# return all the recipes from the database
def get_all_recipes(cursor):
    query = """SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time 
               FROM [dbo].[Recipes] R
               JOIN [dbo].[Users] U ON R.user_id = U.user_id;"""
  
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
    query = """SELECT R.recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time
               FROM [dbo].[Recipes] R
               JOIN [dbo].[Users] U ON R.user_id = U.user_id
               WHERE R.name LIKE ? OR R.description LIKE ?;"""

    search_pattern = f"%{keyword}%"
    cursor.execute(query, (search_pattern, search_pattern))
    results = cursor.fetchall()
    return results if results else None


def get_all_users(cursor):
    cursor.execute("SELECT user_id, full_name FROM Users;")
    return cursor.fetchall()


def get_user(cursor, user_id):
    query = """SELECT user_id, full_name FROM Users WHERE user_id = ?;"""
    cursor.execute(query, user_id)
    result = cursor.fetchone()

    return result if result else None


def get_all_categories(cursor):
    cursor.execute("SELECT category_id, name FROM Category")
    return cursor.fetchall()


def get_category(cursor, category_id):
    query = """SELECT category_id, name FROM Category WHERE category_id = ?;"""
    cursor.execute(query, category_id)
    result = cursor.fetchone()

    return result if result else None
