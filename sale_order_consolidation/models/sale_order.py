# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SalesOrder(models.Model):
    """ create project"""
    _inherit = "sale.order"


    # @api.model
    # def sale_quotation(self):
    #     print("print")




    def action_record(self):
        print("jjj")

        # for order in self:
        #      draft = order.search([('state', '=', 'draft')])
        #      print("draft", draft)
        #      if draft:
        #         # customer =


        for order in self:
            print("oder",order)

            orders = self.env['sale.order.wizard'].write({
                'sale_order_ids': order.ids,
            })

            print("orders",orders)

            customer = order.partner_id.name
            print("customer",customer)

            draft = self.search([('state', '=', 'draft')])









        return {
                    'type': 'ir.actions.act_window',
                    'name': 'dominating order',
                    'res_model': 'sale.order.wizard',
                    'view_mode': 'form',

                    'target': 'new',
                }
