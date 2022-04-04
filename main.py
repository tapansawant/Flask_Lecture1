from flask import Flask

app = Flask(__name__)


@app.route("/")
def Welcome():
    return "Welcome to my website"


@app.route("/Home")
def home():
    return "Dashboard"


@app.route("/gallery")
def Gallery():
    return "Welcome to my gallery"


@app.route("/contact")
def Contact_Page():
    return "Contact Page"


if __name__ == "__main__":
    app.run()
