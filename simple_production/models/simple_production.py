# -*- coding: utf-8 -*-
from odoo import fields, models, api

class SimpleProduction(models.Model):
    _name = 'simple.production'
    _description = 'Simple Production'


    product_id = fields.Many2one('product.product', string='Product', required=True)
    # variant_id = fields.Many2one('product.product', string='Product Variant',)
    quantity = fields.Float(string='Quantity', required=True, default=1)
    state = fields.Selection([
        ('draft', 'Draft'),('created', 'Created'),('done', 'Done')
    ])

    line_ids = fields.One2many('simple.production.line', 'production_id', string='Lines')


    def action_create(self):

        location = self.env.ref('stock.stock_location_stock')
        dest = self.env.ref('stock.stock_location_output')
        print('location', location)
        print('dest', dest)

        production = self.env['stock.location'].search([('usage', '=', 'production')],limit=1)
        print('production', production)

        print("line",self.line_ids)
        for line in self.line_ids:

            stock = self.env['stock.move'].create({
                'product_id': line.product_id.id,
                'product_uom': line.product_id.uom_id.id,
                'product_uom_qty' : line.quantity,
                'location_id': location.id,
                'location_dest_id': production.id,
            })

            print('stock add', stock)
            print("qty",line.product_id.uom_id.id)
            print("line qty",line.quantity)

            # stock._action_confirm()
            # stock._action_assign()

            stock.move_line_ids.write({
                'quantity': line.quantity,
            })
            stock.quantity = line.quantity
            # stock._action_done()




            product = self.env['stock.move'].create({
                'product_id': self.product_id.id,
                'product_uom_qty' : self.quantity,
                'product_uom': self.product_id.uom_id.id,
                'location_id': production.id,
                'location_dest_id': location.id,
            })


            product._action_confirm()
            product.quantity = self.quantity
            product._action_done()



            self.state = 'created'

    #
    #
    # def action_done(self):
    #     print('done')
    #     loc = self.env['stock.move'].search([])
    #     loc._action_done()
    #     self.state = 'done'
        # for record in self:
        # product =  self.env['product.product'].search([('id', '=', self.product_id.id)])
        # print("product",product)









