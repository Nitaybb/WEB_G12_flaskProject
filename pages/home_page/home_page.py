from flask import Blueprint, render_template, redirect, url_for

# home_page blueprint definition
home_page = Blueprint('home_page', __name__, static_folder='static', static_url_path='/home_page', template_folder='templates')


# Routes
@home_page.route('/')
def index():
    return render_template('home_page.html')
