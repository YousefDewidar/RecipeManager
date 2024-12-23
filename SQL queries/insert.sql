use recipe;

-- Insert 10 Categories
INSERT INTO Category (name) VALUES
('Breakfast'), ('Lunch'), ('Dinner'), ('Dessert'), ('Appetizer'),
('Salad'), ('Soup'), ('Side Dish'), ('Beverage'), ('Snack');

INSERT INTO Users (full_name) VALUES
('Alice Johnson'),
('Bob Williams'),
('Charlie Brown'),
('David Garcia'),
('Eva Rodriguez'),
('Frank Martinez'),
('Grace Anderson'),
('Henry Taylor'),
('Ivy Thomas'),
('Jack Moore');

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