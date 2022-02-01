from flask import Blueprint, render_template, redirect, url_for

# products blueprint definition
registeration = Blueprint('registeration', __name__, static_folder='static', static_url_path='/registeration', template_folder='templates')


# Routes
@registeration.route('/registeration')
def index():
    return render_template('registeration.html')
