from wtforms import Form, StringField

class WeatherForm(Form):
    city = StringField("City")
    country_code = StringField("Country Code")
    