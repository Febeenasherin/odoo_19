# -*- coding: utf-8 -*-
from odoo import fields, models, api
import xmlrpc.client
from odoo.exceptions import ValidationError


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"


    # customer_id = fields.Many2one('res.partner', string="Customer")

    sale_order_ids = fields.Many2many('sale.order')










    # def action_order_sale(self):
    #     print("jjj")
    #
    #
    #
    #
    #     return {
    #                 'type': 'ir.actions.act_window',
    #                 'name': 'dominating order',
    #                 'res_model': 'sale.order.wizard',
    #                 'view_mode': 'form',
    #                 'target': 'new',
    #             }

