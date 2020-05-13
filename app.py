# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import getPet,getPetPic


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        activityLevel = request.form["activityLevel"]
        time = request.form["interactionLevel"]
        size = request.form["petSize"]
        pet = getPet(activityLevel, time, size)
        props = {
            "activity": activityLevel,
            "time": time,
            "size": size,
            "pet": pet
        }
        return render_template("results.html", props=props)
    else:
        return "error"
