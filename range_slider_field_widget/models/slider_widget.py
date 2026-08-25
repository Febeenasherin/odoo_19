# -*- coding: utf-8 -*-

# from odoo import fields, models
#
# class ProductProduct(models.Model):
#    _inherit = 'product.product'
#    quality_level = fields.Integer('Quality Level')


from odoo import fields, models


class SliderWidget(models.Model):
    _name = "slider.widget"


    slider = fields.Integer("Slider")

