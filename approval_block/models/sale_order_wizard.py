# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SalesOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "Sales Order Wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")
    quantity = fields.Integer(string="Quantity")
    price = fields.Integer(string="Price")
    product_id = fields.Many2one('product.product', string="Product")

    def action_confirm_order(self):
        self.ensure_one()
        for record in self:
            sale = self.env['sale.order'].search([('partner_id', '=',  record.partner_id.id), ("state" ,'=', 'draft')], limit=1)
            print("sale",sale)

            if not sale:

                sale = self.env['sale.order'].create({'partner_id': self.partner_id.id})
                self.env['sale.order.line'].create({ 'product_template_id': self.product_id.id,
                                                       'product_uom_qty': self.quantity,
                                                       'price_unit': self.price,})


            sale.action_confirm_order()



