# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'


    def action_confirm(self):
        print("hhh")

        #
        # products =self.order_line.mapped('product_id')
        # print("products", products)

        for line in self.order_line:

            vendor = line.product_id.seller_ids[0].partner_id
            print("vendor", vendor)


            print(self.name,"orders")

            rfq = self.env['purchase.order'].create({
                        'partner_id': vendor.id,
                        'origin': self.name,

                        'order_line' : [fields.Command.create({
                            'product_id': line.product_id.id,
                            'name' : line.product_id.name,
                            'product_qty': line.product_uom_qty,
                        })]
                    })


            print(rfq,"rfq")


        return super().action_confirm()








            # sales = self.env['sale.order.line'].search([('product_id', "=", rec.ids)])
            # print(sales,"sales")





