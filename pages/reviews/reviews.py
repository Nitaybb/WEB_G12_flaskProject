from flask import Blueprint, render_template, redirect, url_for

# products blueprint definition
reviews = Blueprint('reviews', __name__, static_folder='static', static_url_path='/reviews', template_folder='templates')


# Routes
@reviews.route('/reviews')
def index():
    return render_template('reviews.html')
