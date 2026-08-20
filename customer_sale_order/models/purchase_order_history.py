# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import fields, models, api


class PurchaseOrderHistory(models.Model):
    _name = 'purchase.order.history'


    sale_id = fields.Many2one('sale.order', string='Sale Order')
    purchase_ids = fields.Many2many('purchase.order', string='Purchase Orders')
    # purchase_ids = fields.One2many('purchase.order', '' string='Purchase Orders')
    partner_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Date(string='Date')
    salesperson_id = fields.Many2one('res.users', string='Sales Person')
    vendor_id = fields.Many2one('res.partner', string='Vendor')


    @api.model
    def action_history(self):
        print("qq")

        yesterday = fields.Date.today() - timedelta(days=1)
        print("yestrday",yesterday)
        today = fields.Date.today()

        order = self.env['sale.order'].search([('date_order', '>=', today), ('date_order', '<=', today), ('state', '=', 'sale')])
        print("order",order)

        # purchase = self.env['sale.order'].search([('date_order', '>=', today), ('date_order', '<=', today)])
        # print("purchase",purchase)


        for rec in order:
            purchase = self.env['purchase.order'].search([('origin', '=', rec.name)])
            print("purchase", purchase)
            print("rec", rec.name)

            self.env['purchase.order.history'].create({
                    'sale_id': rec.id,
                    'purchase_ids': purchase.ids,
                    'partner_id' : rec.partner_id.id,
                    'date' : today,
                    'salesperson_id' : rec.user_id.id,
                    'vendor_id' : purchase[0].partner_id.id

            })






