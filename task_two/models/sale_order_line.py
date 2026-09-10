# -*- coding: utf-8 -*-
from odoo import fields, models, api



class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"


    product_ids = fields.Many2many('product.product', readonly= True, compute= '_compute_sale_order_line', store=True)
    partner_id = fields.Many2one(related = 'order_id.partner_id', readonly = True,)



    @api.depends('product_id','partner_id','partner_id.is_only_ordered')

    def _compute_sale_order_line(self):

        print("kk",self)

        product = self.env['product.product'].search([])

        new = self.partner_id.is_only_ordered
        print("new",new)
        for line in self:
            print("order",line)

            if line.order_id.partner_id.is_only_ordered:
                line.product_ids = self.env['product.product'].search(
                    [('invoice_policy', '=', 'order')])
                print("policy", len(line.product_ids))

            else:
                line.product_ids = product
