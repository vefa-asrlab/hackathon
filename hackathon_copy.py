from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

connection = sqlite3.connect('login.db')
cur = connection.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        print(username, password)
    return render_template("login.html")
