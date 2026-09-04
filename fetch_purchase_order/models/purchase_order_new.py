# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrder(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order"


    # old_po_id = fields.Integer(string="old id")

    purchase_no = fields.Integer(string="Old id")


