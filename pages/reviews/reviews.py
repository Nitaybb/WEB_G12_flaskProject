from flask import Blueprint, render_template, redirect, url_for, request
import mysql.connector
from utilities.classes.review import Review


# products blueprint definition
reviews = Blueprint('reviews', __name__, static_folder='static', static_url_path='/reviews', template_folder='templates')


# Routes
@reviews.route('/reviews')
def index():
    data = Review.getAllRevires()
    return render_template('reviews.html', reviews=data)


@reviews.route('/request', methods=['GET', 'POST'])
def main_func():
    if request.method == 'POST':
        rv = Review(name=request.form['inputName'], comment=request.form['Comment'], rate=request.form['rate'])
        rv.createReview()
    data = Review.getAllRevires()
    return redirect('reviews')
