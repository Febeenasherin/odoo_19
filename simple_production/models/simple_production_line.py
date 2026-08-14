# -*- coding: utf-8 -*-
from odoo import fields, models, api

class SimpleProductionLine(models.Model):
    _name = 'simple.production.line'
    _description = 'Simple Production Line'


    production_id = fields.Many2one('simple.production',)

    product_id = fields.Many2one('product.product', string='Components')
    quantity = fields.Float(string='Quantity', default=1)