# -*- coding: utf-8 -*-
from odoo import fields, models, api



class CustomerPricingLine(models.Model):
    _name = 'customer.pricing.line'

    customer_id = fields.Many2one('res.partner', string='Customer')
    unit_price = fields.Float(string='Unit Price')
    quantity = fields.Float(string='Quantity')
    prod_id = fields.Many2one('product.product', string='Product')

