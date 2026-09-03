# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseMigrationLine(models.Model):
    _name = 'purchase.migration.line'


    product = fields.Char(string="Product")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    amount = fields.Float(string="Amount")
    product_id = fields.Many2one(comodel_name='purchase.migration', string="Product")