# -*- coding: utf-8 -*-
from odoo import fields, models, api



class ProductProduct(models.Model):
    _inherit = "product.product"



    total_sale_count = fields.Integer(string="Total Sale Count", compute="_compute_total_sale_count")


    def _compute_total_sale_count(self):
        print("gg")

        for record in self:
            products = self.env['sale.order.line'].search(
                [('product_id', "=", record.id), ('product_uom_qty', '>', 0), ('order_id.state', '=', 'sale')])

            print(products, "products sold")
            order = products.mapped('order_id')
            print("oder:",order)
            record.total_sale_count = len(order)

        return

    def write(self, vals):
        print("jjj")
        result = super().write(vals)
        if 'lst_price' in vals:
            # for record in self:

                product = self.env['sale.order.line'].search([('product_id', "=", self.id), ('order_id.state', '=', 'draft')])

                print(product,"products sale price")

                product.write({
                    'price_unit' : self.lst_price,
                })

        return result

