# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    """inherit product template"""
    _inherit = "product.template"



    def unlink(self):

        """ product cant delete, that product already used in confirmed sale order """

        product = self.env['sale.order.line'].search([('product_id', '=', self.id), ('state', 'in', ['sale'])])
        print(product)

        if product:
            raise UserError("the product can't be deleted bcs this product already used in confirmed sale order")


        return super().unlink()


    @api.model_create_multi
    def create(self, vals_list):


        """on product creation , the reference will auto crete sequence id , prefix based on category"""
        print("self", self, vals_list)
        for vals in vals_list:
            if not vals.get('default_code'):
                categ_val = self.env['product.category'].browse(vals.get('categ_id'))
                # vl = prefix.prefix
                print(categ_val, "vall")
                if categ_val.prefix_val:
                    print("ddws",categ_val.sequence_id)
                    if not categ_val.sequence_id:

                        sequence = self.env['ir.sequence'].create({
                            'name' : 'product.category-%s' % categ_val.name,
                            'code' : 'product.category.%s' % categ_val.id,
                            'prefix' : "",
                            'number_next' : 1,
                            'number_increment' : 1,
                            'padding' : 3,

                        })

                        print("seq", sequence)


                        categ_val.sequence_id = sequence.id

                    number = categ_val.sequence_id.next_by_id()
                    print("number", number)
                    vals['default_code'] = (f"{categ_val.prefix_val}/{number}")

        return super(ProductTemplate, self).create(vals_list)

    #
    # def copy(self,default=None):
    #     print("copy")
    #
    #     self.default_code = False
    #
    #
    #     return super().copy()



