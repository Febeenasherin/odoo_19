# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    """add field to purchase order"""
    _inherit = "purchase.order.line"

    vendor_id = fields.One2many('purchase.order', 'vendor_products', string="Vendor ID")



    # # if vendor_id True:
    # #
    # #
    # @api.onchange('vendor_products')
    # def _onchange_product_vendor(self):
    #
    #
    #      if self.order_id.vendor_products:
    #     #     print(self.vendor_id)
    #
    #         # self.env['product.supplierinfo'].search([('partner_id', '=', self.partner_id.id)])
    #         #
    #         #
    #         # if self.order_id.seller_ids:
    #             return {
    #                 'domain' : {'product_id' : 'seller_ids.partner_id","=",parent.partner_id'}
    #             }
    #
    #




