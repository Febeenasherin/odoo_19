# -*- coding: utf-8 -*-
from odoo import models, fields


class ExampleLine(models.Model):
    """"""
    _name = 'example.line'
    _description = 'Example Line'

    product = fields.Char(string='Product')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    sub_total = fields.Float(string='Sub Total')
    example_id = fields.Many2one('example')

