# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductionOrderLine(models.Model):
    _name = 'production.order.line'


    order_id = fields.Many2one('production.order',)
    production_id = fields.Many2one('simple.production',)
    line_id = fields.Many2one('simple.production.line', 'Line')


    product_id = fields.Many2one('product.product', 'products')
    quantity_id = fields.Integer('Consume Quantity',default=1)






