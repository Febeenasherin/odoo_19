# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"


    sale_order_ids = fields.One2many('sale.order', 'partner_id', string="Sale Order")

    product_count = fields.Integer(compute='_compute_product_count', string="Product Count")


    def _compute_product_count(self):
        for order in self:
            partner = self.env['sale.order'].search([('partner_id', '=', order.id)])
            print("partner", partner)

            product = partner.mapped('order_line.product_id')
            print("product", product)

            order.product_count=len(product)
            print(order.product_count,"count")



    def action_products(self):
        """ smart button products form view"""

        self.ensure_one()

        partner = self.env['sale.order'].search([('partner_id', '=', self.id)])
        product = partner.mapped('order_line.product_id')


        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'res_model': 'product.product',
            'domain': [('id', '=', product.ids)],
            'view_mode': 'list,form',
        }






