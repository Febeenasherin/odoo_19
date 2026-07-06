# -*- coding: utf-8 -*-
from odoo import fields, models


class ApprovalBlock(models.Model):
    _name = "approval.block"
    _description = "Approval Block"
    _rec_name = "amount_limit"



    approved_by = fields.Many2one('res.partner', string="Approved By")
    amount_limit = fields.Float(string="Amount", required=True)
    approved_date = fields.Date(string="Approved Date")