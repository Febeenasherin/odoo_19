# -*- coding: utf-8 -*-


from odoo import fields, models, api


class SalesOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "Sales Order Wizard"


    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    quantity = fields.Integer(string="Quantity", required=True, default=1)
    price = fields.Integer(string="Price",required=True)
    product_id = fields.Many2one('product.template', string="Product",required=True)

    def action_confirm(self):
        """ while clicking confirm button inside wizard.the quotation is change to sale order"""
        self.ensure_one()

        sale = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id), ("state" ,'=', 'draft')],limit=1)

        if not sale:
            sale = self.env['sale.order'].create({'partner_id': self.partner_id.id})
        sale.write({
            'order_line': [(0, 0, {
                'product_template_id': self.product_id.id,
                'product_uom_qty': self.quantity,
                'price_unit': self.price
            })]
        })
        sale.action_confirm()








