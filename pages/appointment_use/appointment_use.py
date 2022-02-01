from flask import Blueprint, render_template, redirect, url_for

# products blueprint definition
appointment_use = Blueprint('appointment_use', __name__, static_folder='static', static_url_path='/appointment', template_folder='templates')


# Routes
@appointment_use.route('/appointment')
def index():
    return render_template('appointment_use.html')
