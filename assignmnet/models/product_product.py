# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'


    approve = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved')], string='Approved',
                               default='draft',)

    pricing_ids = fields.One2many('customer.pricing.line', 'prod_id', string='Pricing')






