# -*- coding: utf-8 -*-

from odoo import fields,models

class  SalesStatus(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[("admitted","Admitted")])
