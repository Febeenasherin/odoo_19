# -*- coding: utf-8 -*-
from odoo import fields, models, api



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    api_key = fields.Char(string="API Key", required=True, config_parameter='apikey_weather')
    city = fields.Char(string='City', config_parameter='city_weather')
    weather_notification = fields.Boolean(
        string='Weather Notification'
    )


