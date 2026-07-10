# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    # is_vendor_product = fields.Boolean(related='.vendor_products', readonly=True)