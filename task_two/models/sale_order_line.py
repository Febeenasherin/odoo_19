# -*- coding: utf-8 -*-
from exceptions import ValidationError

from odoo import fields, models, api


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"


    product_ids = fields.Many2many('product.product', readonly= True, compute= '_compute_sale_order_line', store=True)
    # partner_id = fields.Many2one(related = 'order_id.partner_id', readonly = True,)

    @api.depends('product_id','order_id.partner_id.is_only_ordered')

    def _compute_sale_order_line(self):

        print("kk",self)

        product = self.env['product.product'].search([])

        new = self.order_id.partner_id.is_only_ordered
        print("new",new)
        for line in self:
            print("order",line)
            print("dd",line.order_id.partner_id.is_only_ordered)

            if line.order_id.partner_id.is_only_ordered:
                line.product_ids = self.env['product.product'].search([('invoice_policy', '=', 'order')])
                print("policy", len(line.product_ids))


            else:
                line.product_ids = self.env['product.product'].search([])

            print('afdasdf',line.product_ids)
            # if line.product_id.invoice_policy != 'order':
            #     raise ValidationError("error")






        # @api.constrains('product_id')
        # def _check_product_id(self):
        #     print("dsdsds")
        #
        #     for line in self:
        #         if line.product_id.is_only_ordered and line.product_id.invoice_policy != 'order':
        #             raise ValidationError("product not select")




