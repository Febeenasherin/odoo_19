# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    approval_block_id = fields.Many2one('approval.block', string="Approval Block", compute="_compute_approval_block_id")


    @api.depends('amount_total')
    def _compute_approval_block_id(self):
        print("nnn")
        for rec in self:
            approval = self.env['approval.block'].search([('amount_limit', '<=', rec.amount_total)], order='amount_limit desc',limit=1)
            rec.approval_block_id = approval

        print("mm",approval)
        print("am",rec.amount_total)

    # if self.approval_block_id >= rec.amount_total:
    #     self.approval_block_id = rec.amount_total

