from flask import Flask, render_template
from data import tours
from data import departures
from data import description
from data import subtitle

app = Flask(__name__)


@app.route("/")
def render_main_page():
    filtered_tours = dict()
    count = 1
    for item in tours.items():
        if count > 6:
            break
        count += 1
        filtered_tours.setdefault(*item)

    return render_template("index.html",
                           tours=filtered_tours,
                           departures=departures,
                           description=description,
                           active_departure=None)


@app.route("/departures/<departure>/")
def render_departures(departure):
    if departure not in departures:
        return render_template('404_error_page.html',
                               departures=departures,
                               active_departure=None), 404

    filtered_tours = {key: value for key, value in tours.items() if value["departure"] == departure}
    return render_template("departure.html",
                           tours=filtered_tours,
                           departures=departures,
                           description=description,
                           subtitle=subtitle,
                           active_departure=departure)


@app.route("/tours/<int:id>/")
def render_tours(id):
    if id not in tours:
        return render_template('404_error_page.html',
                               departures=departures,
                               active_departure=None), 404

    tour = tours[id]
    departure_code = tour["departure"]
    departure_name = departures[departure_code]
    return render_template("tour.html",
                           tour=tour,
                           tour_id=id,
                           departures=departures,
                           departure_name=departure_name,
                           active_departure=departure_code)


@app.route('/buy_tour/<int:id>/')
def render_buy_page(id):
    print(id)
    if id not in tours:
        return render_template('404_error_page.html',
                               departures=departures,
                               active_departure=None), 404
    return render_template('buy_page.html',
                           departures=departures,
                           active_departure=None)


@app.errorhandler(404)
def render_404_error_page(arg):
    print(arg)
    return render_template('404_error_page.html',
                           departures=departures,
                           active_departure=None), 404


if __name__ == '__main__':
    app.run()
