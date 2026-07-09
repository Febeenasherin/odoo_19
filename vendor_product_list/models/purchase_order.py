# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseOrder(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order"

    vendor_products = fields.Boolean(string="Vendor Products")


