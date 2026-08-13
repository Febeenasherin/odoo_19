# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date

from odoo.tests import result


class MaterialRequestLine(models.Model):
    """school student registration"""
    _name = 'material.request.line'
    _description = 'Material Request Line'


    request_id = fields.Many2one('material.request', string="Request_id")
    product_id = fields.Many2one('product.product', string="Product", required=True)
    product_qty = fields.Integer("Quantity", required=True, default=1)
    request_type = fields.Selection([('purchase order', 'Purchase Order'),('internal transfer' ,'Internal Transfer')], required=True)
    vendor_ids = fields.Many2many('res.partner', string="Vendors", required=True)
    source_id = fields.Many2one('stock.location', string="Source location",)
    destination_id = fields.Many2one('stock.location', string="Destination location",)


    @api.onchange('product_id')
    def _onchange_vendor_id(self):
        print("working")

        if self.product_id:
            vendor = self.product_id.seller_ids.mapped('partner_id')
            print(vendor)
            self.vendor_ids = vendor

            # for rec in vendor:
            #     rec.vendor_ids = [rec.name]
            #
            #     print(rec.vendor_ids)


