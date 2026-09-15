# -*- coding: utf-8 -*-
from odoo import fields, models



class ProductProduct(models.Model):
    """inherit product template"""
    _inherit = "product.category"



    prefix_val = fields.Char(string="Prefix")
    sequence_id = fields.Many2one('ir.sequence', string="Sequence",copy=False, readonly=True)