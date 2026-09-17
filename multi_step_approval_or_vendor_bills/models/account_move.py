# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"



    state = fields.Selection(selection_add=([('submitted', 'Submitted'), ('finance_approved', 'Finance Approved'),
                                            ('cfo_approved', 'CFO Approved')]), ondelete={'submitted': 'set default',
                                                                                                        'finance_approved': 'set default',
                                                                                                          'cfo_approved': 'set default',})

    status_in_payment = fields.Selection(selection_add=([('submitted', 'Submitted'),('finance_approved', 'Finance Approved'),
                                                         ('cfo_approved', 'CFO Approved'),]))


    def action_finance_approve(self):

        """clicking button the state changed to finance approve"""

        if not self.env.user.has_group('account.group_account_manager'):
            raise UserError("Only manager can approve")

        self.state = 'finance_approved'
        self.status_in_payment = 'finance_approved'


    def action_submitted(self):

        """clicking button the state changed to submit"""


        # for rec in self:
        #     if rec.move_type != 'in_invoice':
        #         raise ValidationError("error")

        # if not self.env.user.has_group('account.group_account_user'):
        #     raise UserError("Only user can submit")

        self.state = 'submitted'
        self.status_in_payment = 'submitted'


        return True


    def action_cfo_approve(self):
        """clicking button the state changed to cfo approve"""
        if not self.env.user.has_group('multi_step_approval_or_vendor_bills.account_cfo_approver'):
            raise UserError("Only CFO User can approve")
        self.state = 'cfo_approved'
        self.status_in_payment = 'cfo_approved'


        return True


    def action_post(self):
        """clicking button the state changed to post, override post"""

        res = super().action_post()

        if self.state == 'cfo_approved':

            self.state = 'post'



        return res



