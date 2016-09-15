import requests

class OpenWeatherAPI ():
    def __init__ (self, api_key, units = "imperial"):
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.base_payload = {
            "appid" : api_key,
            "units" : units,
        }

    def get_payload(self, **kwargs):
        payload = {}

        for key, value in self.base_payload.items():
            payload[key] = value

        for key, value in kwargs.items():
            payload[key] = value

        return payload


    def get_current_weather (self, city, country_code = ""):
        q = ""

        if country_code:
            q = "{}, {}".format(city, country_code)
        else:
            q = city

        payload = self.get_payload(q=q)
        url = "{}{}".format(self.base_url, "/weather")
        r = requests.get(url, params=payload)
        result = result_or_error(r.json())

        return  DailyWeather(
                description = result["weather"][0]["description"],
                icon = result["weather"][0]["icon"],
                temp = result["main"] ["temp"], 
                dt = result["dt"],
                wind = result["wind"]["speed"],
                pressure = result ["main"]["pressure"],
                humidity = result ["main"]["humidity"],
                sunrise = result ["sys"]["sunrise"],
                sunset = result ["sys"]["sunset"],
            )


    def get_weather_forecast(self, city, country_code="", num_days=16):
        q = ""

        if country_code:
            q = "{}, {}".format(city, country_code)
        else:
            q = city

        payload = self.get_payload(q=q, cnt=num_days)

        url = "{}{}".format(self.base_url, "/forecast/daily")
        r = requests.get(url, params=payload)
        result = result_or_error(r.json())
        weather_list []

        for item in result["list"]:
            daily_weather = DailyWeather(
                    icon = item["weather"][0]["icon"],
                    description = item["weather"][0]["description"],
                    temp = item["temp"]["day"],
                    temp_night = item["temp"]["night"],
                    dt = item ["dt"],
                    pressure = item["pressure"],
                    humidity = item ["humidity"],
                )
            weather_list.append(daily_weather)
            
        return result

        # return  DailyWeather(
        #         description = result["weather"][0]["description"],
        #         icon = result["weather"][0]["icon"],
        #         temp = result["main"] ["temp"], 
        #         dt = result["dt"],
        #         wind = result["wind"]["speed"],
        #         pressure = result ["main"]["pressure"],
        #         humidity = result ["main"]["humidity"],
        #         sunrise = result ["sys"]["sunrise"],
        #         sunset = result ["sys"]["sunset"],
        #     )        



class DailyWeather ():
    
    def __init__(self,
        description = "",
        icon = None,
        dt = None, 
        temp=None,
        temp_night = None,
        wind= None, 
        pressure = None,
        humidity = None,
        sunrise = None,
        sunset = None,
        ):

        self.description = description
        self.icon = icon
        self.dt = dt
        self.temp = temp
        self.temp_night = temp_night
        self.wind = wind
        self.pressure = pressure
        self.humidity = humidity
        self.sunrise = sunrise
        self.sunset = sunset

    def __str__(self):
        return "Description: {}, Temp: {}".format(self.description, self.temp)

def result_or_error(result):
    if str(result.get("cod")) != "200":
        raise ValueError("City not found.")

    return result








        

