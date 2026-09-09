# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SalesOrder(models.Model):
    _inherit = "sale.order"





    def _action_update_delivery(self):


        if len(self) <= 2:
            raise ValidationError("Order must be greater than 2")

        for order in self:
            print("order", order)
            # new = order.filtered(lambda o: o.state == 'draft' or o.state == 'send')
            # print("new", new)

            if order.state in ['cancel', 'sale']:
                print("order", order.state)
                raise ValidationError("only draft and quotation send select")


            number = len(order)
            print("number", number)







        return {
            'type': 'ir.actions.act_window',
            'name': 'Update delivery',
            'res_model': 'sale.order.wizard.delivery',
            'view_mode': 'form',
            'context': {'default_sale_order_ids': self.ids},
            'target': 'new',
        }


