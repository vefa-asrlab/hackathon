from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/login", view_func=views.login)
app.add_url_rule("/hackathon", view_func=views.hackathon)
app.add_url_rule("/login/submit", view_func=views.submit_login, methods=["POST"])
