from main import app
from flask import render_template
# rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/gpt")
def blog():
    return "sai daqui."
