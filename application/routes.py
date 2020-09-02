from application import app #imports from the __init__ file
from flask import render_template, request

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html", index=True)  #render_template function

@app.route("/login")
def login():
	return render_template("login.html", login=True)  #render_template function

@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
	courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, 
	{"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, 
	{"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
	{"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
	{"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
	print(courseData)
	return render_template("courses.html", courseData=courseData, courses=True, term=term)  #render_template function

@app.route("/register")
def register():
	return render_template("register.html", register=True)  #render_template function

@app.route("/enrollment")     #getting data from the form in enrollment using the get method
def enrollment():
	id = request.args.get('courseID')
	title = request.args.get('title')
	term = request.args.get('term')
	return render_template("enrollment.html", enrollment=True, data={"id":id, "title":title,"term":term}) 