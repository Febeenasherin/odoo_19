# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    """ add field to product. template"""
    _inherit = 'product.template'


    brand = fields.Char(string="Brand")

    @api.model
    def _load_pos_data_fields(self, config_id):
        """
        Adds the 'brand' field to the list of fields loaded into the POS.
        """
        data = super()._load_pos_data_fields(config_id)
        print("data",data)
        data += ['brand']
        print("add data",data)
        return data

