from flask import current_app, render_template, redirect, url_for, request
import sqlite3


def index():
    return render_template("index.html")

def hackathon():
    return render_template("hackathon.html")

def login():
    return render_template("login.html")

def submit_login():

    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()

    # Create variables for easy access
    username = request.form['username']
    password = request.form['password'] # Check if account exists using MySQL
    
    cursor.execute('SELECT * FROM login WHERE user_id = %s AND password = %s', (username, password,))
    # Fetch one record and return result
    account = cursor.fetchone()
    # If account exists in accounts table in out database
    if account:
        # Create session data, we can access this data in other routes
        # session['loggedin'] = True
        # session['username'] = account['user_id']
        # session['password'] = account['password']
        # Redirect to home page
        return redirect(url_for("hackathon"))
    else:
        # Account doesnt exist or username/password incorrect
        return = 'Incorrect username/password!'

    
