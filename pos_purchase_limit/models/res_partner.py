# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    """ add field to pos customer form"""
    _inherit = "res.partner"


    is_purchase_limit = fields.Boolean('Purchase Limit')
    purchase_limit = fields.Float('limit')

    ActionpadWidget