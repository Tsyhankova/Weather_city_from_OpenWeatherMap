import pprint
import requests
from dateutil.parser import parse


class OpenWeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=47a2c817f1f3f4de9927b237ae6b3c10"
        print('sending HTTP request')
        data = requests.get(url).json()
        forecast_data = data["main"]
        forecast = forecast_data["temp"]
        self._city_cache[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherForecast()
    
    def weather_forecast(self):
        return self._weather_forecast.get(self.city)
        

def _main():
    weather_forecast = OpenWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Wroclaw", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == '__main__':
    _main()