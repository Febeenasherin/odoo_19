# -*- coding: utf-8 -*-
from itertools import count

from odoo import models, fields, api
from datetime import datetime,timedelta


class ProductProduct(models.Model):
    """ product auto archive"""
    _inherit = 'product.product'

    # product_id = fields.Many2one('sale.order.line')
    # active = fields.Boolean(string='active', default=True )

    def auto_product_archive(self):
        """ schedule action,archive product not sold last 90 day"""
        products = self.search([('active', '=', True)])
        today = datetime.today()
        last_day = today - timedelta(days=90)
        print(today)


        sold =self.env['sale.order.line'].search([('order_id.state', 'in', 'sale')])

        print("sold",sold)

        for product in products:
            sold_product = sold.filtered(lambda line: line.product_id == product and line.order_id.date_order >= last_day)

            print("sold_product",sold_product)

            if not sold_product:
                product.active = False



































