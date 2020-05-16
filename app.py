from flask import Flask

app = Flask(__name__)


@app.route("/")
def render_main_page():
    return "<h3>Тут будет главная страница</hl3>"


@app.route("/departures/<departure>/")
def render_departures(departure):
    return "<h3>Тут будут направления</hl3>"


@app.route("/tours/<id>/")
def render_tours(id):
    return "<h3>Тут будут туры</hl3>"


app.run('0.0.0.0', 8000, debug=True)
