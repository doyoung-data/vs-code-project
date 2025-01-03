from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/id")
def id():
    return render_template("id-class.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

if __name__ == "__main__":
    app.run(debug=True)