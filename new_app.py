from flask import Flask, flash, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome"

@app.route("/hello")
def hello():
	return "Hello World!!"

@app.route("/trek")
def star_trek():
        return "Live long and Prosper!!"

@app.route("/wars")
def star_wars():
        return "May the force be with you!!"

@app.route("/hello/<string:name>/")
def getName(name):
        return render_template(
		'new_view.html',name=name)


if __name__ == "__main__":
	app.run()


