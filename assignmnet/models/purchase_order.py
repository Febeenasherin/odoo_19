# -*- coding: utf-8 -*-
from odoo import fields, models, api

class PurchaseOrder(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order"




    @api.onchange('partner_id')
    def _onchange_product(self):
        print("fdf")
        for order in self:
            produt = order.product_id
            print("pro",produt)






































