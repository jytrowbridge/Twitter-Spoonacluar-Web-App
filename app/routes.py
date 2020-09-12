from flask import Flask, render_template, request

from app import app
from app.static.scripts.random_recipe import get_random_recipe
from app.static.scripts.twitter_recipe_search import search_twitter
from app.static.scripts.search_recipes import search_recipes


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

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_query = ""
    search_results = []
    if request.method == 'POST':
        search_query = request.form.get('search-value')
        search_results = search_recipes(search_query)
        if len(search_results) == 0:
            search_results = [-1]

    return render_template(
        'search.html',
        search_query=search_query,
        search_results=search_results
    )
