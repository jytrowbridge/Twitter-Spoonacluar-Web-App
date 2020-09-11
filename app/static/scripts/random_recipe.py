from dotenv import load_dotenv
#import json
import os
import requests

load_dotenv()

API_KEY = os.getenv('SPOONACULAR_API_KEY')
params = {'apiKey': API_KEY}


def get_random_recipe():
    try:
        response = requests.get(
            "https://api.spoonacular.com/recipes/random",
            params=params
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    resp_json = response.json()
    recipe = resp_json['recipes'][0]
    return {
        'title': recipe['title'],
        'image_url': recipe['image'],
        'source_url': recipe['sourceUrl']
    }
