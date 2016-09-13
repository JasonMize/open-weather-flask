from flask import render_template, request

from app import app
from app.forms import WeatherForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET", "POST"])
def current_weather ():
    weather_form = WeatherForm(request.form)

    return render_template('current.html', 
        weather_form = weather_form)

@app.route("/forecast", methods=["GET", "POST"])
def forecast_weather ():
    weather_form = WeatherForm(request.form)
    return render_template('forecast.html', 
        weather_form = weather_form)

