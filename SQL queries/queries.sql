CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1), -- IDENTITY for auto-increment in T-SQL
    full_name VARCHAR(255)
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
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Ingredients (
    ingredient_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255)
);

CREATE TABLE Recipe_Ingredients (
    recipe_id INT,
    ingredient_id INT,
    quantity DECIMAL(10, 2),
    unit VARCHAR(50),
    PRIMARY KEY (recipe_id, ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    recipe_id INT,
    review_text TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id)
);