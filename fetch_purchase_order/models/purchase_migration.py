# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseMigration(models.Model):
    _name = 'purchase.migration'


    old_id = fields.Char(string='Old ID')
    name = fields.Char(string='Reference')
    vendor_name = fields.Char(string='Vendor')
    date_order = fields.Date(string='Date Order')
    amount_total = fields.Float(string='Amount Total')
    line_ids = fields.One2many('purchase.migration.line', 'product_id')


