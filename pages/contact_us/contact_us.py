from flask import Blueprint, render_template, redirect, url_for

# products blueprint definition
contact_us = Blueprint('contact_us', __name__, static_folder='static', static_url_path='/contact_us', template_folder='templates')


# Routes
@contact_us.route('/contact_us')
def index():
    return render_template('contact_us.html')
