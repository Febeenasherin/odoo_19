# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrder(models.Model):
    """add status in sale module"""
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[("admitted", "Admitted")])

