use recipe;

-- Insert 10 Categories
INSERT INTO Category (name) VALUES
('Breakfast'), ('Lunch'), ('Dinner'), ('Dessert'), ('Appetizer'),
('Salad'), ('Soup'), ('Side Dish'), ('Beverage'), ('Snack');

INSERT INTO Users (full_name, age, email) VALUES
('Alice Johnson', 25, 'alice.johnson@example.com'),
('Bob Williams', 30, 'bob.williams@example.com'),
('Charlie Brown', 22, 'charlie.brown@example.com'),
('David Garcia', 35, 'david.garcia@example.com'),
('Eva Rodriguez', 28, 'eva.rodriguez@example.com'),
('Frank Martinez', 40, 'frank.martinez@example.com'),
('Grace Anderson', 27, 'grace.anderson@example.com'),
('Henry Taylor', 33, 'henry.taylor@example.com'),
('Ivy Thomas', 29, 'ivy.thomas@example.com'),
('Jack Moore', 31, 'jack.moore@example.com');


INSERT INTO Recipes (name, description, cooking_time, user_id, category_id) VALUES
('Pancakes', 'Fluffy breakfast pancakes', 15, 1, 1),
('Chicken Salad Sandwich', 'Classic lunch sandwich', 10, 2, 2),
('Spaghetti Bolognese', 'Hearty Italian dinner', 45, 3, 3),
('Chocolate Cake', 'Rich chocolate dessert', 60, 4, 4),
('Bruschetta', 'Toasted bread with tomatoes and basil', 20, 5, 5),
('Caesar Salad', 'Classic salad with romaine lettuce', 15, 6, 6),
('Tomato Soup', 'Comforting tomato soup', 30, 7, 7),
('Mashed Potatoes', 'Creamy mashed potatoes', 25, 8, 8),
('Lemonade', 'Refreshing summer drink', 5, 9, 9),
('Popcorn', 'Simple movie snack', 5, 10, 10)

INSERT INTO Ingredients (name) VALUES
('Eggs'),('Cheese'),('Tuna'),('Bread'),('Chicken'),('Vegetables'),
('Apples'),('Cinnamon'),('Spinach'),('Tortilla Chips'),('Feta Cheese'),
('Lettuce'),('Noodles');

INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit) VALUES
(1, 1, 2, 'pcs'),(1, 2, 100, 'g'),(2, 3, 1, 'can'),(2, 4, 2, 'slices'),(3, 5, 200, 'g'),
(3, 6, 150, 'g'),(4, 7, 3, 'pcs'),(4, 8, 1, 'tsp'),(5, 9, 100, 'g'),(5, 10, 50, 'g'),
(6, 11, 100, 'g'),(6, 12, 1, 'head'),(7, 13, 200, 'g'),(7, 1, 2, 'pcs'),(8, 2, 150, 'g'),
(8, 3, 1, 'can'),(9, 4, 2, 'slices'),(9, 5, 200, 'g'),(10, 6, 150, 'g'),(10, 7, 3, 'pcs');


-- Insert Reviews
INSERT INTO Reviews (user_id, recipe_id, review_text, star_rating) VALUES
(1, 1, 'Delicious pancakes, perfect for breakfast!', 5),
(2, 1, 'Good but a bit too sweet for my taste.', 4),
(3, 2, 'The chicken salad sandwich is very tasty and quick to make.', 5),
(4, 3, 'Spaghetti Bolognese had a great flavor, but took longer than expected.', 4),
(5, 4, 'Rich and moist chocolate cake! A family favorite.', 5),
(6, 5, 'Bruschetta was fresh and flavorful, but needed more seasoning.', 3),
(7, 6, 'Caesar Salad is a classic. The dressing was excellent.', 5),
(8, 7, 'Tomato soup was comforting, but slightly too acidic.', 4),
(9, 8, 'Mashed potatoes were creamy and delicious.', 5),
(10, 9, 'Lemonade was refreshing, but a bit too sweet for me.', 4),
(1, 10, 'Popcorn was perfect for our movie night. Easy to make!', 5);
