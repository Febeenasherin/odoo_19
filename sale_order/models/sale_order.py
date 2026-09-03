# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_quotation_send(self):

        # order = self.env['sale.order'].search([('id', '=' ,self.id)])
        # print("order", order)
        # order_line = order.order_line
        # print("orderline", order_line)
        #
        # print("order_line", self.order_line)

        for order in self:

            if not order.order_line:
                raise ValidationError("give orderline")
        return super().action_quotation_send()



    def action_confirm(self):
        for order in self:
            product = order.order_line.product_id
            print("product", product)

            for prod in product:

                print("prod", prod)

                if prod:

                    added = prod.product_restrict_ids
                    print("added", added)

                    for lines in added:


                        if lines in product:
                            raise ValidationError("product cant added")


        return super().action_confirm()
