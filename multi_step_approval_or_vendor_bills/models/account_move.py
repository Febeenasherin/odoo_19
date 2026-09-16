# -*- coding: utf-8 -*-
from odoo import fields, models

class AccountMove(models.Model):
    _inherit = "account.move"



    state = fields.Selection(selection_add=[('submitted', 'Submitted'), ('finance_approved', 'Finance Approved'),
                                            ('cfo_approved', 'CFO Approved')], ondelete={'submitted': 'set default',
                                                                                         'finance_approved': 'set default',
                                                                                         'cfo_approved': 'set default'})




    def action_finance_approve(self):

        self.status_in_payment = 'finance_approved'

    def action_submitted(self):

        self.status_in_payment = 'submitted'