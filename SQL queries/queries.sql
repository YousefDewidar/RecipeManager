CREATE DATABASE recipe;

use recipe;

CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    full_name VARCHAR(255),
    age INT,
    email VARCHAR(255)
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255)
);

CREATE TABLE Recipes (
    recipe_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255),
    description TEXT,
    cooking_time INT,
    user_id INT,
    category_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Ingredients (
    ingredient_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) UNIQUE
);

CREATE TABLE Recipe_Ingredients (
    recipe_id INT,
    ingredient_id INT,
    quantity DECIMAL(10, 2),
    unit VARCHAR(50),
    PRIMARY KEY (recipe_id, ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id) ON DELETE CASCADE
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY IDENTITY(1,1),
    reviewer_name TEXT,
    recipe_id INT,
    star_rating INT,
    review_text TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id) ON DELETE CASCADE
);



CREATE PROCEDURE spGetRecipeById 
@recipe_id INT 
AS
BEGIN 
	SELECT recipe_id, U.full_name as author_name, R.name, R.description, R.cooking_time, R.user_id, R.category_id, C.name as category_name
	FROM [dbo].[Recipes] R
	join [dbo].[Users] U on R.user_id = U.user_id
	join [dbo].[Category] C on R.category_id = C.category_id
	WHERE R.recipe_id = @recipe_id
end

