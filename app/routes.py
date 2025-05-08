from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/hello")
def hello():
    return {"message": "Hello from Flask!"}