# -*- coding: utf-8 -*-
from odoo import fields, models, api



class PurchaseOrderLine(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order.line"

    is_vendor_product = fields.Boolean(related = 'order_id.vendor_products', readonly= True)
    product_ids = fields.Many2many('product.product', readonly= True, compute= '_compute_purchase_order_line')
    partner_id = fields.Many2one(related = 'order_id.partner_id', readonly = True,)
    # is_vendor_product = fields.Boolean(related = 'order_id.vendor_products', readonly= True)
    #


    @api.depends('product_id','is_vendor_product','partner_id')

    def _compute_purchase_order_line(self):
        """ when enable is vendor product , only show product corresponding vendor"""
        print("kk",self)

        product = self.env['product.product'].search([])
        for order in self:
                if order.is_vendor_product:
                    order.product_ids = self.env['product.product'].search(
                        [('seller_ids.partner_id', '=', order.partner_id.id)])

                else:
                    order.product_ids = product






















# @api.onchange('product_id')
    # def _onchange_product_vendor(self):
    #     print("jjj",self)
    #
    #     """when enable is product vendor ,show only vendor products."""
    #     if self.is_vendor_product and self.partner_id:
    #         print("jjj",self.partner_id)
    #         print("en",self.is_vendor_product)
    #
    #
    #         domain = ([('seller_ids.partner_id', '=', self.partner_id.id)])
    #
    #         print("partner",domain)
    #
    #     else:
    #         domain = []
    #
    #     return {'domain': {'product_id' : domain}}
    # #
    # # values = _onchange_product_vendor()
    # # print(values)
    #





            # return {
            #     'domain' : {'product_id': [('seller_ids.partner_id', '=', self.partner_id.id)]}}
            #


        #
        # return {
        #     'domain': {'product_id': []}
        #     }











