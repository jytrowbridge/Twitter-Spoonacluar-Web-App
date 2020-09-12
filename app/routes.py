from flask import render_template

from app import app
from app.static.scripts.random_recipe import get_random_recipe
from app.static.scripts.twitter_recipe_search import search_twitter


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/random')
def random():
    recipe = get_random_recipe()
    tweets = search_twitter(recipe['title'])

    if len(tweets) == 0:
        tweets = search_twitter((' ').join(recipe['title'].split(' ')[0:2]))

    return render_template(
        'show_recipe.html',
        recipe=recipe,
        tweets=tweets
    )

@app.route('/search')
def search():
    return render_template(
        'search.html'
    )
