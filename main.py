from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Welcome():
    return "<h1> Welcome </h1>"


@app.route("/Home")
def home():
    return "Dashboard"


@app.route("/gallery")
def Gallery():
    return "Welcome to my gallery"


@app.route("/contact")
def Contact_Page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
