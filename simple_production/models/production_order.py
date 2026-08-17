# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductionOrder(models.Model):
    _name = 'production.order'
    _description = 'Manufacturing Order'



    name = fields.Char(copy=False, required=True, default='New')
    product_id = fields.Many2one(
        'product.product', 'Product',
        compute='_compute_product_id', store=True, readonly=False,)

    bom_id = fields.Many2one(
        'simple.production', 'Bill of Material', )

    quantity = fields.Float('Quantity', store=True, readonly=False)

    state = fields.Selection([
        ('draft', 'Draft'), ('produce', 'Produced'),
    ])

    production_line_ids = fields.One2many('production.order.line', 'order_id', 'Production Lines')
    line_id = fields.Many2one('simple.production.line', 'Line')
    # production_line_ids = fields.One2many('simple.production.line', 'order_id', 'Lines')
    order_id = fields.Many2one('simple.production.line', 'Order')



    @api.onchange('bom_id')
    def _onchange_bom_id(self):

        # products = self.env['simple.production'].search([])
        #
        self.production_line_ids = [(5, 0, 0)]
        #     print(self.production_line_ids)


        values=[]

        for line in self.bom_id.line_ids:
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



    def action_produce(self):
        """" when clicking create button the main product stock will move from production to warehouse and component product move from
               whare house to production"""

        location = self.env.ref('stock.stock_location_stock')
        dest = self.env.ref('stock.stock_location_output')
        print('location', location)
        print('dest', dest)

        production = self.env['stock.location'].search([('usage', '=', 'production')], limit=1)
        print('production', production)

        print("line", self.production_line_ids)
        for line in self.production_line_ids:
            stock = self.env['stock.move'].create({
                'product_id': line.product_id.id,
                'product_uom': line.product_id.uom_id.id,
                'product_uom_qty': line.quantity_id,
                'location_id': location.id,
                'location_dest_id': production.id,
            })

            print('stock add', stock)
            print("qty", line.product_id.uom_id.id)
            print("line qty", line.quantity_id)

            stock._action_confirm()

            stock.picked = True
            stock._action_assign()

            stock.move_line_ids.write({
                'quantity': line.quantity_id,
            })
            stock.quantity = line.quantity_id
            stock._action_done()

        product = self.env['stock.move'].create({
            'product_id': self.product_id.id,
            'product_uom_qty': self.quantity,
            'product_uom': self.product_id.uom_id.id,
            'location_id': production.id,
            'location_dest_id': location.id,
        })

        product._action_confirm()
        product.picked = True
        product.quantity = self.quantity
        product._action_done()

        self.state = 'produce'

    @api.model_create_multi
    def create(self, vals_list):
        """ sequence"""

        print("self", self, vals_list)
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals["name"] = self.env['ir.sequence'].next_by_code('namee') or 'New'

        return super(ProductionOrder, self).create(vals_list)