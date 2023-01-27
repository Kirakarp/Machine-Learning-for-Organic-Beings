# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 17:16:47 2023

@author: detec
"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/index")
def index():
        return render_template("index.html")

@app.route("/learn")
def learn():
        return render_template("learn.html")

@app.route("/project")
def project():
        return render_template("project.html")

@app.route("/contact")
def contact():
        return render_template("contact.html")


if __name__ == "__main__":
	app.run() 