from wtforms import Form, StringField, validators, ValidationError

class WeatherForm(Form):

    city = StringField("City", validators=[validators.DataRequired()])
    country_code = StringField("Country Code")

    def validate_city(form, field):
        if field.data == "assdf":
            raise ValidationError ("Watcha doin' Willis?")
