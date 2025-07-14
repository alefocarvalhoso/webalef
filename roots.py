from main import app
from flask import render_template
# rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/test")
def tests():
    return render_template("no.html")

@app.route("/love")
def lovepag():
    return render_template("love.html")