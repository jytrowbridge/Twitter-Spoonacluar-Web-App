from dotenv import load_dotenv
import os
from app.static.scripts.get_request import get_request

load_dotenv()

API_KEY = os.getenv('SPOONACULAR_API_KEY')
params = {'apiKey': API_KEY}

url = "https://api.spoonacular.com/recipes/complexSearch"


def search_recipes(query):
    # Return list of recipes from Spoonacular api given search query.
    # Returns list of recipes. Each recipe has following attributes:
    #   id
    #   title
    #   image
    #   imageType

    params['query'] = query
    resp_json = get_request(
        url,
        params=params
    )

    return resp_json['results']
