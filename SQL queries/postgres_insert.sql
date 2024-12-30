-- Authors
INSERT INTO authors (full_name, age, email) VALUES
('Sarah Jones', 32, 'sarah.jones@email.com'),
('David Miller', 45, 'david.miller@email.com'),
('Omar El-Sayed', 28, 'omar.elsayed@email.com'),
('Amina Hassan', 50, 'amina.hassan@email.com'),
('Michael Lee', 24, 'michael.lee@email.com'),
('Emily Davis', 38, 'emily.davis@email.com'),
('John Smith', 60, 'john.smith@email.com'),
('Jessica Wilson', 29, 'jessica.wilson@email.com'),
('Robert Brown', 42, 'robert.brown@email.com'),
('Ashley Garcia', 35, 'ashley.garcia@email.com'),
('William Rodriguez', 55, 'william.rodriguez@email.com'),
('Elizabeth Martinez', 27, 'elizabeth.martinez@email.com'),
('James Anderson', 48, 'james.anderson@email.com'),
('Jennifer Taylor', 31, 'jennifer.taylor@email.com'),
('Christopher Thomas', 52, 'christopher.thomas@email.com'),
('Linda Jackson', 26, 'linda.jackson@email.com'),
('Daniel White', 40, 'daniel.white@email.com'),
('Angela Harris', 37, 'angela.harris@email.com'),
('Matthew Martin', 58, 'matthew.martin@email.com'),
('Melissa Thompson', 23, 'melissa.thompson@email.com');

-- Category
INSERT INTO category (name) VALUES
('Breakfast'), ('Lunch'), ('Dinner'), ('Dessert'), ('Appetizers'),
('Egyptian'), ('Italian'), ('Indian'), ('Greek'), ('Moroccan'),
('American'), ('Mexican'), ('Chinese'), ('Thai'), ('Japanese'),
('French'), ('Spanish'), ('Vietnamese'), ('Korean'), ('British');

-- Recipes
INSERT INTO Recipes (name, description, cooking_time, user_id, category_id) VALUES
('Pancakes', 'Light and fluffy pancakes perfect for breakfast.', 20, 1, 1),
('Grilled Cheese Sandwich', 'A classic comfort food with melted cheese.', 15, 2, 2),
('Spaghetti Bolognese', 'Hearty pasta dish with meat sauce.', 45, 3, 3),
('Chocolate Chip Cookies', 'Chewy and delicious cookies with chocolate chips.', 20, 4, 4),
('Hummus', 'Creamy chickpea dip, a staple of Middle Eastern cuisine.', 30, 3, 6),
('Koshari', 'Egyptian national dish with rice, lentils, and pasta.', 45, 3, 6),
('Chicken Tikka Masala', 'Spicy Indian dish with chicken in a creamy tomato sauce.', 40, 5, 8),
('Stir-Fried Vegetables', 'Quick and healthy dish with mixed vegetables.', 20, 1, 2),
('Moussaka', 'Greek casserole with layers of eggplant, meat, and sauce.', 60, 2, 9),
('Apple Pie', 'Classic American dessert with apples and a flaky crust.', 60, 4, 11),
('Falafel', 'Deep-fried chickpea fritters, popular in the Middle East.', 30, 3, 6),
('Tagine', 'Moroccan stew with meat, vegetables, and spices.', 90, 5, 10),
('Pizza', 'Italian classic with various toppings.', 30, 1, 7),
('Chicken Curry', 'Indian dish with chicken in a flavorful curry sauce.', 40, 2, 8),
('Baklava', 'Rich dessert with layers of filo pastry, nuts, and honey.', 60, 3, 6),
('Salmon with Roasted Vegetables', 'Healthy and delicious meal with salmon and veggies.', 30, 4, 2),
('Sushi', 'Japanese dish with vinegared rice and various toppings.', 45, 5, 15),
('Beef Stew', 'Hearty comfort food with beef, vegetables, and gravy.', 120, 1, 3),
('Pasta Primavera', 'Italian dish with pasta and fresh spring vegetables.', 30, 2, 7),
('Ful Medames', 'Egyptian dish of cooked fava beans served with oil and spices.', 30, 3, 6);


-- Ingredients
INSERT INTO Ingredients (name) VALUES
('Flour'), ('Sugar'), ('Eggs'), ('Milk'), ('Butter'),
('Cheese'), ('Bread'), ('Ground Beef'), ('Tomato Sauce'), ('Pasta'),
('Chocolate Chips'), ('Chickpeas'), ('Lentils'), ('Rice'), ('Chicken'),
('Vegetables'), ('Eggplant'), ('Apples'), ('Filo Pastry'), ('Nuts'),
('Honey'), ('Salmon'), ('Rice Vinegar'), ('Seaweed'), ('Beef'),
('Potatoes'), ('Carrots'), ('Onions'), ('Garlic'), ('Spices'),
('Olive Oil'), ('Lemon'), ('Parsley'), ('Cilantro'), ('Cumin'),
('Coriander'), ('Turmeric'), ('Ginger'), ('Chili Powder'), ('Salt'),
('Pepper'), ('Yeast'), ('Baking Powder'), ('Vanilla Extract');


-- Recipe_Ingredients (Example - you would need more entries to link all recipes to ingredients)
INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity, unit) VALUES
(1, 1, 2, 'cups'), (1, 2, 1/4, 'cup'), (1, 3, 2, ''), (1, 4, 1, 'cup'), (1, 5, 2, 'tbsp'),
(2, 6, 2, 'slices'), (2, 7, 2, 'slices'), (2, 5, 1, 'tbsp'),
(3, 8, 1, 'lb'), (3, 9, 1, 'jar'), (3, 10, 1, 'lb'),
(5, 12, 1, 'can'), (5, 31, 2, 'tbsp'), (5, 32, 1, 'tbsp'),
(6, 13, 1/2, 'cup'),(6, 14, 1, 'cup'),(6, 10, 1/2, 'cup'),
(11,12,1,'cup'),(11,31,2,'tbsp'),(11,33,1,'bunch'),
(15,19,1,'package'),(15,20,1,'cup'),(15,21,1/2,'cup');


-- Reviews (Example)
INSERT INTO Reviews (reviewer_name, recipe_id, star_rating, review_text) VALUES
('John Doe', 1, 5, 'These pancakes were amazing! So fluffy.'),
('Jane Smith', 2, 4, 'A classic, always satisfying.'),
('Peter Jones', 3, 3, 'Good, but could use more seasoning.'),
('Alice Johnson', 5, 5, 'The best hummus I have ever had!'),
('Bob Williams', 6, 4, 'A great introduction to Egyptian cuisine.'),
('Eva Brown', 11, 5, 'Crispy and delicious falafel!'),
('Frank Davis', 15, 4, 'Sweet and nutty, perfect for dessert.');