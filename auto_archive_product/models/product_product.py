# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date,timedelta


class SaleOrder(models.Model):
    _inherit = 'product.product'

    product_id = fields.Many2one('sale.order.line')
    active = fields.Boolean(string='sale_ok.active', default=True, compute='_compute_active', store=True)

    @api.depends('product_id')
    def _compute_active(self):
        for record in self:
            today = date.today()
            last_day = today - timedelta(days=90)

            print("tdy",today)
            print("tdy",last_day)



        if record in self:
            self.env['sale.order.line'].search([('product_id', '!=', record.product_id), ('order_id.state', '=' , 'draft,send')
                                                    ,('date_order', '>=', last_day)])





            for rec in record:
                rec.write({'active': False})





            # product = self.env['product.product'].search([('product_id', 'not in', product.product_id.id)])
            #
            # ids_from_sale = product.mapped('product_id')
            # dates = self.env['sale.order'].search([('date_order', '>=', last_day), ('state', '>=', 'done'), ('id', 'in', ids_from_sale)])

            #
            # for record in dates:
            #     record.write({'active': False})


















    # from datetime import datetime, timedelta
    #
    # # 1. Calculate the date threshold (5 days ago)
    # five_days_ago = datetime.now() - timedelta(days=5)
    #
    # # 2. Find all product IDs sold within the last 5 days
    # recent_move_lines = self.env['stock.move.line'].search([
    #     ('date', '>=', five_days_ago),
    #     ('state', '=', 'done'),
    #     ('picking_code', '=', 'outgoing')
    # ])
    # sold_product_ids = recent_move_lines.mapped('product_id').ids
    #
    # # 3. Filter products not in that list
    # unsold_products = self.env['product.product'].search([
    #     ('id', 'not in', sold_product_ids),
    #     ('type', '=', 'product')  # Optional: limits to storable products
    # ])














