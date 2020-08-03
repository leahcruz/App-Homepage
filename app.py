# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# You'll need this late
from datetime import datetime
# from model import
# import os


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/home')
def index():
    time = datetime.now()
    return render_template("home.html", time = time)


@app.route('/home2')
def home():
    return render_template("home2.html")


@app.route('/resources')
def resources():
    time = datetime.now()
    return render_template("resources.html", time = time)


@app.route('/action')
def action():
    time = datetime.now()
    return render_template("action.html", time = time)

# Form page
@app.route('/map')
def map():
    time = datetime.now()
    return render_template("map.html", time = time)

# Location result
@app.route('/map-result')
def map2():
    return render_template("map-result.html")

@app.route('/profile')
def profile():
    time = datetime.now()
    return render_template("profile.html", time = time)

@app.route('/login')
def login():
    time = datetime.now()
    return render_template("login.html", time = time)

# Random Profiles
@app.route('/profile-@annie.schmidt')
def profile1():
    time = datetime.now()
    return render_template("annie.html", time = time)


@app.route('/profile-@mason.williams')
def profile2():
    time = datetime.now()
    return render_template("mason.html", time = time)

@app.route('/profile-@thomas.cohen')
def profile3():
    time = datetime.now()
    return render_template("thomas.html", time = time)

@app.route('/profile-@nina.demeny')
def profile4():
    time = datetime.now()
    return render_template("nina.html", time = time)

@app.route('/profile-@jeffrey.palm')
def profile5():
    time = datetime.now()
    return render_template("jeffrey.html", time = time)

@app.route('/profile-@sofia.montez')
def profile6():
    time = datetime.now()
    return render_template("sofia.html", time = time)


@app.route('/discussions')
def discussions():
    time = datetime.now()
    return render_template("discussions.html", time = time)