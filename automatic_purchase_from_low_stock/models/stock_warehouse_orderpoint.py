# -*- coding: utf-8 -*-
from odoo import fields, models, api

class StockWarehouseOrderPoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    # def action_replenish_auto(self):
    #     print("working")
    # #     # print(self.product_id)
    # #     # for rec in self:
    # #     #     print(rec)
    # #
    # #     # for rec in self.product_id:
    # #         # products = self.env['product.product'].search(['product_id', '=', rec.product_id])
    # #         # print(rec)
    #     self.trigger = 'auto'
    #     return self.action_replenish()


    @api.model
    def create_purchase(self):
        print("working",self)

        rule = self.search([])
        print(rule)


        for order in rule:
            print(order.product_id,"products")
            print(order.product_id.qty_available,"available")
            if order.product_id.qty_available < order.product_min_qty:
                order.action_replenish()


        # product = self.search([('qty_on_hand', '>', 0)])
        # print("product",product)












    # @api.model
    # def _auto_create_purchase(self):
    #     """ automatically send email to employees ,email send 2 day before starting event"""
    #     print("working")
    #     print(self)
    #     qty = self.qty_on_hand
    #     print(qty)
    #
    #     for product in self.product_id:
    #         print(product)















        # class ProductProduct(models.Model):
        #     _inherit = 'product.product'
        #
        #     def action_create_automated_reordering_rule(self):
        #         """Programmatically creates an automatic reordering rule for a product."""
        #         for product in self:
        #             # Ensure the product has a supplier configured, otherwise the 'Buy' route fails
        #             if not product.seller_ids:
        #                 continue
        #
        #             # Fetch the default warehouse or a specific destination warehouse
        #             warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)], limit=1)
        #             if not warehouse:
        #                 continue
        #
        #             # Create the Reordering Rule (Orderpoint)
        #             self.env['stock.warehouse.orderpoint'].create({
        #                 'name': f"Auto PO Rule for {product.name}",
        #                 'product_id': product.id,
        #                 'location_id': warehouse.lot_stock_id.id,  # Primary stock location
        #                 'product_min_qty': 5.0,  # Threshold to trigger PO
        #                 'product_max_qty': 20.0,  # Target stock level after PO
        #                 'qty_multiple': 1.0,  # Order batches (multiples of X)
        #                 'trigger': 'auto',  # Crucial: set to 'auto' for automated RFQ generation
        #                 'route_id': self.env.ref('purchase.route_warehouse0_buy').id,  # Standard 'Buy' route ID
        #             })
