# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = "product.template"

    def action_sale_order(self):
        """."""
        return {'type': 'ir.actions.act_window',
                'name': ('sale order'),
                'res_model': 'sale.order.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_product_id': self.id},
                }

