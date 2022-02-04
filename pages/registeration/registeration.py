from flask import Blueprint, render_template, redirect, url_for, request
import mysql.connector
from utilities.db.db_manager import dbManager
# products blueprint definition


registeration = Blueprint('registeration', __name__, static_folder='static', static_url_path='/registeration', template_folder='templates')


# Routes
@registeration.route('/registeration')
def index():
    return render_template('registeration.html')


def interact_db(query, query_type: str):
    return_value = False
    # creating a connection to the db
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Nitay12345',
                                         database='web-project-g12')
    #  db cursor - this object executes sql queries
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


#### Insert new user to users table ####
@registeration.route('/insert_new_user', methods=['POST'])
def insert_new_users():
    email = request.form['EmailRe']
    first_name = request.form['FirstNameRe']
    last_name = request.form['LastNameRe']
    phone_number = request.form['phoneNumberRe']
    query = "INSERT INTO users(email, first_name, last_name, phone_number) VALUES ('%s', '%s', '%s', '%s')" % (email, first_name, last_name, phone_number)
    interact_db(query=query, query_type='commit')
    return redirect('/registeration')
