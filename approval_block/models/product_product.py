# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    average_cost = fields.Float(string="Average Cost", compute="_compute_average_cost")
    # product = fields.Many2one('purchase.order.line', required=True)


    def _compute_average_cost(self):
        for rec in self:
            tot_cost = 0
            tot_qnty = 0
            lines = self.env['purchase.order.line'].search([('product_id', '=', rec.id)])
            for line in lines:
                tot_qnty += line.product_qty
                tot_cost += line.product_qty * line.price_unit
                # print("cost",tot_cost)
                # print("qnty",tot_qnty)

            if tot_qnty :
                rec.average_cost = tot_cost / tot_qnty

            else:
                rec.average_cost = 0

            


















