# -*- coding: utf-8 -*-
from odoo import fields,models, api
import requests
from datetime import date

class WeatherNotification(models.Model):
    _name = "weather.notification"


    @api.model
    def get_weather(self, latitude, longitude):
        print("weather")

        url = "https://api.openweathermap.org/data/2.5/weather?"

        # api_key = "ecce2d1d8762057bf306d613724829ab"

        api = self.env['res.config.settings'].search([])
        key = api.api_key
        city = api.city
        print(key)
        print(city)

        if city:
            url_city = "http://api.openweathermap.org/data/2.5/weather?"

        value = {
            'appid': key,
            'units': 'metric',
            'lat' : latitude,
            'lon' : longitude,
        }

        data = requests.get(url, params=value).json()
        print(data)

        icon = data['weather'][0]['icon']
        icon_url = "http://openweathermap.org/img/wn/" + icon + "@2x.png"
        print(icon_url)

        temp = data['main']['temp']
        degree = (temp-32) / (5/9)

        return {

            'data' : data,
            'date' : date.today(),
            'weather' : data['weather'][0]['description'],
            'icon' : icon_url,
            'location' : data['name'],
            'temp': temp,

        }
