# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseOrder(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order"

    vendor_products = fields.Boolean(string="Vendor Products")
    # product_id = fields.Many2one(related="order_id.product_id", string="Product")




