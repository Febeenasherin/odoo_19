# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    """ create project"""
    _inherit = "sale.order"





    def _action_record(self):
        print("jjj")
        print(self)

        partner = []
        if len(self) <= 1:
            raise ValidationError("Sales Order cannot be created")
        for order in self:
            print("oder",order)

            if order.state != 'draft':
                raise ValidationError("only select draft orders")


            if len(partner) == 0:
                partner.append(order.partner_id)

            elif partner[0] != order.partner_id:
                raise ValidationError("partner id is different from order")






        return {
                    'type': 'ir.actions.act_window',
                    'name': 'dominating order',
                    'res_model': 'sale.order.wizard',
                    'view_mode': 'form',
                    'context': {'default_sale_order_ids' : self.ids,
                        'default_partner_id' : partner[0].id,},
                    'target': 'new',
                }
