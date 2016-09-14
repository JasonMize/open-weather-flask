from wtforms import Form, StringField, RadioField, validators, ValidationError

class WeatherForm(Form):

    city = StringField("City", validators=[validators.DataRequired()])
    country_code = StringField("Country Code")
    units = RadioField("Units", 
        default = "imperial",
        choices = [
            ("imperial", "imperial", ),
            ("metric", "metric", )
        ])

    def validate_city(form, field):
        if field.data == "assdf":
            raise ValidationError ("Watcha doin' Willis?")
