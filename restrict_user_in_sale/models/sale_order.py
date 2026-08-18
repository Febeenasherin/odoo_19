# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        if self.amount_total > 50000:
            if not self.env.user.has_group('sales_team.group_sale_manager'):
                raise  UserError("manager can only confirm order")


        return super().action_confirm()


