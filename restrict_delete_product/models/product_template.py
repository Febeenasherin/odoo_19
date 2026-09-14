# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    """inherit product template"""
    _inherit = "product.template"



    def unlink(self):

        product = self.env['sale.order.line'].search([('product_id', '=', self.id), ('state', 'in', ['sale'])])
        print(product)

        if product:
            raise UserError("the product can't be deleted bcs this product already used in confirmed sale order")


        return super().unlink()


    @api.model_create_multi
    def create(self, vals_list):
        """add reg_no number"""
        print("self", self, vals_list)
        for vals in vals_list:


            categ_val = self.env['product.category'].browse(vals['categ_id'])
            # vl = prefix.prefix
            print(categ_val, "vall")

            prefix = categ_val.prefix_val
            print(prefix)

            sequence_no = self.env['ir.sequence'].next_by_code('product.sequence') or '/'

            vals['default_code'] = f"{prefix}/{sequence_no}"

        return super(ProductTemplate, self).create(vals_list)