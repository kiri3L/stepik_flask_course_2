from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def render_main_page():
    return render_template("index.html")


@app.route("/departures/<departure>/")
def render_departures(departure):
    return render_template("departure.html")


@app.route("/tours/<id>/")
def render_tours(id):
    return render_template("tours.html")


app.run('0.0.0.0', 8000, debug=True)
