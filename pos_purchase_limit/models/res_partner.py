# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    """ add field to pos customer form"""
    _inherit = "res.partner"


    is_purchase_limit = fields.Boolean('Purchase Limit')
    purchase_limit = fields.Float('limit')


    @api.model
    def _load_pos_data_fields(self, config_id):
        """
        Adds the 'is_purchase_limit and purchase limit' field to the list of fields loaded into the POS.
        """
        data = super()._load_pos_data_fields(config_id)
        print("data", data)
        data += ['is_purchase_limit', 'purchase_limit']
        print("add data", data)
        return data
