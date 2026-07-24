# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """  add sale ordr line"""
    _inherit = 'sale.order'
    def action_confirm(self):
        """  when clicking confirm trigger this function,add delivery product in sale order line untaxed amound is less than 1500"""
        self.ensure_one()
        # delivery = self.env.ref("auto_add_delivery.delivery_product").product_variant_id
        # print("jj",delivery.name)
        if self.amount_untaxed < 1500:
            self.order_line = [fields.Command.create({
                'product_id':  self.env.ref("auto_add_delivery.delivery_product").product_variant_id.id,
            }),]
        return super().action_confirm()
