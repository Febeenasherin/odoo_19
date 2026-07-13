# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """inherit product template"""
    _inherit = "product.template"



    def action_sale_order(self):
        """while clicking button inside product view ,show popup"""
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'name': ('Sale order'),
                'res_model': 'sale.order.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_product_id': self.product_variant_id.id,
                            'default_price' : self.list_price
                            },
                }

