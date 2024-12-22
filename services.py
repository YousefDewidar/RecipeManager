# return all the recipes from the database
def get_all_recipes(cursor):
    query = f"""SELECT full_name as auther_name,name, description, cooking_time 
  FROM [dbo].[Recipes] ,[dbo].[Users]
  WHERE recipes.user_id= Users.user_id;"""

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_all_users(cursor):
    cursor.execute("SELECT user_id, full_name FROM Users")
    return cursor.fetchall()


def get_all_categories(cursor):
    cursor.execute("SELECT category_id, name FROM Category")
    return cursor.fetchall()


#! Not Used Now


# Retrieve the search name and perform a search in the database
def search_recipe(cursor, keyword):
    query = f"""SELECT * 
            FROM recipes 
            WHERE name LIKE '%{keyword}%\'"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results


# Update the recipe details in the database
def update_recipe(cursor, conn, recipe_id, recipe_name, quantity, price):
    query = f"""UPDATE recipes 
                SET name='{recipe_name}', quantity={quantity}, price={price} 
                WHERE recipe_id={recipe_id}"""
    cursor.execute(query)
    conn.commit()


# Delete the recipe from the database
def delete_recipe(cursor, conn, recipe_id):
    readQuery = f"""SELECT * 
                    FROM recipes 
                    WHERE recipe_id = {recipe_id}"""

    cursor.execute(readQuery)
    exists = cursor.fetchall()

    if len(exists) > 0:
        query = f"DELETE FROM recipes WHERE recipe_id={recipe_id}"
        cursor.execute(query)
        conn.commit()
        return True
    else:
        return False
