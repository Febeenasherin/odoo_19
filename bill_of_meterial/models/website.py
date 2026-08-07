# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Website(models.Model):
    _inherit = 'website'

    bom_product_ids = fields.Many2many('product.template', string='BOM Products')

    # @api.model
    # def get_values(self):
    #     #     """Get the values from settings."""
    #     product = self.env['product.template'].search([('product_id', '=', self.id)], limit=1)
    #     res = super(Website, self).get_values()
    #     selected_product = self.bom_product_ids
    #     print("prod",selected_product)
    #
    #     return res