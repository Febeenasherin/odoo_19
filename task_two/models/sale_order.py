# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SalesOrder(models.Model):
    _inherit = "sale.order"


    def action_confirm(self):

        res = super(SalesOrder, self).action_confirm()

        for order in self:

            invoice =  order._create_invoices()

            if invoice:

                invoice.action_post()

        return res