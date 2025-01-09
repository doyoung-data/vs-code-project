from flask import Flask, render_template

app = Flask(__name__)

@app.route("/detail-todo")
def detaileTodo():
    return render_template("detail-todo.html")

@app.route("/js-basic")
def js():
    return render_template("js-basic.html")

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

@app.route("/front")
def front():
    return render_template("front.html")

if __name__ == "__main__":
    app.run(debug=True)