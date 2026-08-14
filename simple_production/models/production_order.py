# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductionOrder(models.Model):
    _name = 'production.order'
    _description = 'Manufacturing Order'

    product_id = fields.Many2one(
        'product.product', 'Product',
        compute='_compute_product_id', store=True, readonly=False,)

    bom_id = fields.Many2one(
        'simple.production', 'Bill of Material', )

    quantity = fields.Float('Quantity', store=True, readonly=False)

    state = fields.Selection([
        ('draft', 'Draft'), ('produce', 'produced'),
    ])

    production_line_ids = fields.One2many('production.order.line', 'order_id', 'Production Lines')
    line_id = fields.Many2one('simple.production.line', 'Line')
    # production_line_ids = fields.One2many('simple.production.line', 'order_id', 'Lines')
    order_id = fields.Many2one('simple.production.line', 'Order')



    @api.onchange('bom_id')
    def _onchange_bom_id(self):

        # products = self.env['simple.production'].search(['product_id', 'in', self.bom_id.id])

        if not self.production_line_ids:
            print(self.production_line_ids)


        values=[]

        for line in self.production_line_ids.line_id:
            values.append((0, 0, {
            'product_id' : line.product_id.id,
            'quantity_id' : line.quantity,
            }))

        self.production_line_ids = values

        print(values)








    @api.depends('bom_id')
    def _compute_product_id(self):
        for production in self:
            bom = production.bom_id
            if bom and (
                    not production.product_id
                    or bom.product_id and bom.product_id != production.product_id
            ):
                production.product_id = bom.product_id