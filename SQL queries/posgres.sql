CREATE TABLE public.authors (
  user_id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  age INT,
  email VARCHAR(255) UNIQUE
);

CREATE TABLE public.category (
  category_id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE public.Recipes (
  recipe_id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  cooking_time INT,
  user_id INT REFERENCES public.authors(user_id) ON DELETE CASCADE,
  category_id INT REFERENCES public.category(category_id),
  CONSTRAINT fk_recipes_author FOREIGN KEY (user_id) REFERENCES public.authors(user_id) ON DELETE CASCADE,
  CONSTRAINT fk_recipes_category FOREIGN KEY (category_id) REFERENCES public.category(category_id) ON DELETE CASCADE
);

CREATE TABLE public.Ingredients (
  ingredient_id SERIAL PRIMARY KEY,
  name VARCHAR(255) UNIQUE
);

CREATE TABLE public.Recipe_Ingredients (
  recipe_id INT,
  ingredient_id INT,
  quantity DECIMAL(10, 2),
  unit VARCHAR(50),
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES public.Recipes(recipe_id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES public.Ingredients(ingredient_id) ON DELETE CASCADE
);

CREATE TABLE public.Reviews (
  review_id SERIAL PRIMARY KEY,
  reviewer_name TEXT,
  recipe_id INT REFERENCES public.Recipes(recipe_id) ON DELETE CASCADE,
  star_rating INT,
  review_text TEXT,
  is_edited BOOLEAN DEFAULT FALSE
);