from lib.database_connection import DatabaseConnection
from lib.recipe_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe_library.sql")

repository = RecipeRepository(connection)
recipes = repository.all()

for recipe in recipes:
    print(recipe)
    
print(repository.find(3))