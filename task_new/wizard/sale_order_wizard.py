# -*- coding: utf-8 -*-
from odoo import fields, models, api
import xmlrpc.client
from odoo.exceptions import ValidationError


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard.delivery"



    new_delivery_date = fields.Datetime(string="New Delivery Date")
    sale_order_ids = fields.Many2many('sale.order')
    reason = fields.Char(string="Reason")

    def action_update(self):

        print("bb")
        print("new",self.new_delivery_date)

        order = self.sale_order_ids
        print("order",order)

        total = len(order)


        for rec in order:
            date = rec.validity_date
            print("date",date)

            rec.write({
                'commitment_date': self.new_delivery_date,
            })

        # length = len(rec)

            rec.message_post(
                body=(f" the reason for updating delivery: {self.reason}"),
                message_type ='comment',

                # partner_ids=[user.id],
            )

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Date Update Confirmed!',
                'message': f'Update{total} delivery date has been successfully confirmed.',
                'type': 'success',  # Blue success notification,
                'sticky': False,  # Auto-dismiss after a few seconds
                'next': {'type': 'ir.actions.act_window_close'}
            }
        }
        # return {
        #     'name': 'update order',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'sale.order',
        #     'view_mode': 'list,form',
        #
        #     'target': 'current',
        #
        # }










