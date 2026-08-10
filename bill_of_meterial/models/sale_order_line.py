# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    bom_component = fields.Text(string='BoM Component', compute='_compute_bom_component', store=True)


    @api.depends('product_id',)
    def _compute_bom_component(self):
        for line in self:
            print("hjk")
            print(line)

            line.bom_component = ''

            website = line.order_id.website_id

            products = line.product_id
            print("product",products)
            print("website",website)

            product = self.env['res.config.settings'].search([])
            select_product = product.bom_product_ids
            print("product",product)
            print("select_product",select_product)
            for rec in select_product:
                print("rec",rec.name)
                if rec in products:

                    bom = self.env['mrp.bom'].search([('product_id', '=', rec.id)], )
                    print("bom:",bom)



                    if bom:
                        for bom_line in bom.bom_line_ids:
                            line.bom_component += (bom_line.product_id.display_name + ' - ' + str(bom_line.product_qty) + "\n")

                            print(line.bom_component)

