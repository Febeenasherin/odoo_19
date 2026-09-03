# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'


    product_restrict_ids = fields.Many2many('product.product', relation='accounaccount_payment_rel',
        column1='product_id',
        column2='product2_id',string="Product not add")