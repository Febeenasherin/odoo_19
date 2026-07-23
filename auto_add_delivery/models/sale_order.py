# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """  add sale ordr line"""
    _inherit = 'sale.order'
    def action_confirm(self):
        """  when clicking confirm trigger this function,add delivery product in sale order line untaxed amound is less than 1500"""
        self.ensure_one()
        produ =self.env['product.product'].search([('name' , '=', "Local delivery")],limit=1)
        if self.amount_untaxed < 1500:
            self.env['sale.order.line'].create({
                    'order_id': self.id,
                    'product_id': produ.id,})
        print ("pro",produ)
        return super().action_confirm()
