from flask import Blueprint, render_template, redirect, url_for, request
import mysql.connector
from utilities.db.db_manager import dbManager
# products blueprint definition


registeration = Blueprint('registeration', __name__, static_folder='static', static_url_path='/registeration', template_folder='templates')


# Routes
@registeration.route('/registeration')
def index():
    return render_template('registeration.html')


#### Insert new user to users table ####
@registeration.route('/insert_new_user', methods=['POST'])
def insert_new_users():
    email = request.form['EmailRe']
    first_name = request.form['FirstNameRe']
    last_name = request.form['LastNameRe']
    phone_number = request.form['phoneNumberRe']
    gender = request.form['GendarSelectRe']
    query = "INSERT INTO users(first_name, last_name, phone_number, email, gender) VALUES ('%s', '%s', '%s', '%s', '%s')" % (first_name, last_name, phone_number, email, gender);
    dbManager.commit(query)
    return redirect('/registeration')
