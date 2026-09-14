# -*- coding: utf-8 -*-
from odoo import fields, models



class ProductProduct(models.Model):
    """inherit product template"""
    _inherit = "product.category"



    prefix_val = fields.Char(string="Prefix")