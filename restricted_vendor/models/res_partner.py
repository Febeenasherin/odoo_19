# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    """ add field to customer form"""
    _inherit = "res.partner"



    restricted = fields.Boolean(string="Restricted")
    restricted_count = fields.Integer(string="Restricted Count")


