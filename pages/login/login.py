from flask import Blueprint, render_template, redirect, url_for, request

# products blueprint definition
from utilities.db.db_manager import dbManager

login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')


@login.route('/user_login', methods=['POST'])
def user_login():
    phone_number = request.form['PhoneNumberCon']
    email = request.form['EmailCon']
    query = "INSERT INTO users(first_name, last_name, phone_number, email, gender) VALUES ('%s', '%s', '%s', '%s', '%s')" % (first_name, last_name, phone_number, email, gender);
    dbManager.fetch(query)
    return redirect('/')
