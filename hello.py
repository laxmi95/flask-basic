from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Live long and prosper!!"
 
if __name__ == "__main__":
    app.run()
