from dotenv import load_dotenv
import os
from app.static.scripts.get_request import get_request

load_dotenv()

API_KEY = os.getenv('SPOONACULAR_API_KEY')
params = {'apiKey': API_KEY}

url = "https://api.spoonacular.com/recipes/random"


def get_random_recipe():
    # Return random recipe from spoonacular API.
    # Return value is a dictionary with following properties:
    #   'title' : the title of the recipe
    #   'image_url' : the url of the image for the recipe
    #   'source_url' : the url of the original recipe source

    resp_json = get_request(
        url,
        params=params
    )
    recipe = resp_json['recipes'][0]
    return {
        'title': recipe['title'],
        'image_url': recipe['image'],
        'source_url': recipe['sourceUrl']
    }
