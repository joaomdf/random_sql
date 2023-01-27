As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).


nouns
recipes, names, cooking_time, rating

Record     Properties
recipes    names, cooking_time_in_minutes, rating

database => recipe_directory_db

id: SERIAL PRIMARY KEY
average_cooking_time: int
rating: int (from 1 to 5)
CHECK rating BETWEEN 1 AND 5