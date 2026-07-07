from odoo import fields, models, api


class ProductOrderLine(models.Model):
    _inherit = "purchase.order.line"

    cost = fields.Many2one('product.product', required=True)