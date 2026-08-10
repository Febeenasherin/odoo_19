# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.release import product_name


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    bom_product_ids = fields.Many2many(related='website_id.bom_product_ids',string='Products',readonly=False)


