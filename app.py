import os
from flask import Flask, redirect, url_for, render_template
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    
    return page
    
@app.route("/home/")    
def home():
    return render_template("index.html")
    
@app.route("/<niem>")
def user(niem):
    return render_template("index.html", content=niem)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))