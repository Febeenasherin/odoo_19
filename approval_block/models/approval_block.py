# -*- coding: utf-8 -*-
from odoo import fields, models


class ApprovalBlock(models.Model):
    """ approval block model"""
    _name = "approval.block"
    _description = "Approval Block"
    _rec_name = "amount_limit"

    name = fields.Char(string="Name", required=True)
    amount_limit = fields.Float(string="Amount", required=True)
