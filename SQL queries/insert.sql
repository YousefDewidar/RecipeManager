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
INSERT INTO Reviews (recipe_id, reviewer_name, review_text, star_rating)
VALUES
(1, 'Ahmed', 'The recipe was amazing! Loved the flavors and how easy it was to follow.', 5),
(2, 'Sara', 'It turned out great! However, I added a bit more salt to suit my taste.', 4),
(3, 'Mohamed', 'Not bad, but I think the cooking time was a bit too long for my liking.', 3),
(4, 'Lina', 'I love this recipe! Simple and delicious, I will make it again.', 5),
(5, 'Omar', 'I wasn’t too fond of the taste. I think I’ll try a different recipe next time.', 2),
(6, 'Mona', 'Great recipe, but I had to substitute a few ingredients due to availability. Still tasted great!', 4),
(7, 'Yasmin', 'It was okay, but I found the recipe to be a bit too complicated for beginners.', 3),
(8, 'Tariq', 'The best recipe I’ve tried this month. Easy and quick to prepare, highly recommend!', 5),
(9, 'Fatima', 'It’s good, but the portion size was a bit too much for me. I’ll reduce it next time.', 4),
(10, 'Karim', 'I didn’t like the recipe much, the texture didn’t turn out right. Maybe it’s just me.', 2);

