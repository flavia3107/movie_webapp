from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reserve")
def reserve():
    return render_template("reserve.html")

@app.route("/movie")
def movie():
    return render_template("movie.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sailing")
def sailing():
    return render_template("sailing.html")

@app.route("/highlights")
def highlights():
    return render_template("highlights.html")

@app.route("/walking")
def walking():
    return render_template("walking.html")
# @app.route("/path")
# def test():
# return redirect(url_for("movie", var=varMew))


if __name__ == "__main__":
    app.run()