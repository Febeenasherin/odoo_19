# -*- coding: utf-8 -*-
from odoo import fields, models, api

class SimpleProduction(models.Model):
    _name = 'simple.production'
    _description = 'Simple Production'


    product_id = fields.Many2one('product.product', string='Product', required=True)
    # variant_id = fields.Many2one('product.product', string='Product Variant',)
    quantity = fields.Float(string='Quantity', required=True, default=1)
    state = fields.Selection([
        ('draft', 'Draft'),('created', 'Created')
    ])

    line_ids = fields.One2many('simple.production.line', 'production_id', string='Lines')


    def action_create(self):

        self.state = 'created'
        # for record in self:
        product =  self.env['product.product'].search([('id', '=', self.product_id.id)])
        print("product",product)









