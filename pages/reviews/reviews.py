from flask import Blueprint, render_template, redirect, url_for, request
import mysql.connector
from utilities.classes.review import reviews

# products blueprint definition
reviews = Blueprint('reviews', __name__, static_folder='static', static_url_path='/reviews', template_folder='templates')


# Routes
@reviews.route('/reviews')
def index():
    return render_template('reviews.html')


@reviews.route('/request', methods=['GET', 'POST'])
def main_func():
    if request.method == 'POST':
        rv = reviews()
        rv.name = request.form['inputName']
        rv.Comment = request.form['Comment']
        # rv.stars_rate = request.form['stars_rate']
        rv.info()
    return redirect('/reviews')
