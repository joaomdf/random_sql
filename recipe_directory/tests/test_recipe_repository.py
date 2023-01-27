from lib.recipe_repository import *

def test_recipe_all(db_connection):
    db_connection.seed('seeds/recipe_library.sql')
    repository = RecipeRepository(db_connection)
    assert repository.all() == [
        Recipe(1, 'Francesinha', '60 min', 5),
        Recipe(2, 'Butter Chicken', '90 min', 5),
        Recipe(3, 'Dried Ass Chicken', 'Who knows, who cares', 1),
        Recipe(4, 'Stir-fry', '30 min', 4)
        ]

def test_recipe_find_three(db_connection):
    db_connection.seed('seeds/recipe_library.sql')
    repository = RecipeRepository(db_connection)
    assert repository.find(3) == Recipe(3, 'Dried Ass Chicken', 'Who knows, who cares', 1)