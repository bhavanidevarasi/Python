
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"
    
@app.route("/about")
def about():
    return "About Page"
app.run()
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Bhavani"
    )
'''