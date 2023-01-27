from lib.recipe import *

def test_recipe_creates_args():
    recipe = Recipe(1,"Francesinha", "90 min", 5)
    assert recipe.id == 1
    assert recipe.name == "Francesinha"
    assert recipe.average_cooking_time == "90 min"
    assert recipe.rating == 5

def test_recipe_formatted_nicely():
    recipe = Recipe(1,"Francesinha", "90 min", 5)
    assert str(recipe) == "Recipe(1, Francesinha, 90 min, 5)"

def test_recipe_compares_two_objects_with_same_args_as_equal():
    recipe1 = Recipe(1,"Francesinha", "90 min", 5)
    recipe2 = Recipe(1,"Francesinha", "90 min", 5)
    assert recipe1 == recipe2