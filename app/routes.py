from flask import render_template

from app import app
from app.static.scripts.random_recipe import get_random_recipe


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/random')
def random():
    recipe = get_random_recipe()
    return render_template('random.html', recipe=recipe)
