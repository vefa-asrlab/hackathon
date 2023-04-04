from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/hackathon")
def hackathon():
    return render_template("hackathon.html")

@app.route("/count")
def hackathon():
    return render_template("count.html")
