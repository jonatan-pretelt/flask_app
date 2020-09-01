from application import app #imports from the __init__ file
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html")  #render_template function

@app.route("/login")
def login():
	return render_template("login.html")  #render_template function

@app.route("/courses")
def courses():
	return render_template("courses.html")  #render_template function

@app.route("/register")
def register():
	return render_template("register.html")  #render_template function